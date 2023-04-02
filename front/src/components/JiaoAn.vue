<template>
  <div>    

        <h3>社团教案</h3>
        <el-upload
          class="upload-demo"
          ref="upload"
          action="http://127.0.0.1:5000/upload_mult/subject_name/dirname"
          :on-preview="handlePreview"
          :on-remove="handleRemove"
          :file-list="fileList"
          :auto-upload="false"
          :headers="set_headers"
          :multiple="true"
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
            只能上传jpg/png文件，且不超过500kb
          </div>
        </el-upload>
  
   
  </div>
</template>
 
 <script>
export default {
  data() {
    return {
      fileList: [],
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
  },
};
</script>
 