<template>
  <div>    

        <h3>社团教案</h3>
        <el-upload
          class="upload-demo"
          ref="upload"
          :action="request_url"
          :on-preview="handlePreview"
          :on-remove="handleRemove"
          :file-list="fileList"
          :auto-upload="false"
          :headers="set_headers"
          :multiple="true"
          :before-upload="beforeUpload"
          :on-success="show_success"
        >
          <el-button slot="trigger" size="small" type="primary"
            >选取文件</el-button
          >
          <el-button
            style="margin-left: 10px"
            size="small"
            type="success"
            @click="submitUpload"
            >上传到服务器</el-button
          >
          <div slot="tip" class="el-upload__tip">
            只能上传doc/docx文件
          </div>
        </el-upload>
  
   
  </div>
</template>
 
 <script>
 import { Message } from 'element-ui';
export default {
  data() {
    return {
      fileList: [],
      request_url: this.$store.state.back_url + "/upload_mult/subject_name/dirname", 
       set_headers:  {
          token: localStorage.getItem('token'),
          subject_name: encodeURIComponent(localStorage.getItem('subject_name')),
          dirname: encodeURIComponent("课时教案")
        }
    };
  },
  methods: {
    submitUpload() {
      this.$refs.upload.submit();
    },
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePreview(file) {
      console.log(file);
    },
    
    show_success(){
      this.$message.success('上传成功')
    },
    beforeUpload(file){
     if(file.type!=='application/vnd.openxmlformats-officedocument.wordprocessingml.document' &&  file.type!=='application/msword'){
      Message({
          message: "只能选择.docx文件或者.doc文件",
          type:"warning"
        })
        return false
     }
     return true
    }
  },
};
</script>
 