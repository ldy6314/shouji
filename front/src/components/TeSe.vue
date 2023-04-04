<template>
  <div>
    
   <h3>
    特色活动方案
   </h3>
   <el-upload
  class="upload-demo"
  ref="upload"
  :action="request_url"
  :on-preview="handlePreview"
  :on-success="show_success"
  :on-remove="handleRemove"
  :file-list="fileList"
  :headers="set_headers1"
  :before-upload="beforeUpload"
  :auto-upload="false">
  <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
  <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
  <div slot="tip" class="el-upload__tip">只能上传doc/docx文件，且不超过500kb</div>

</el-upload>
  <h3>
    特色活动照片（过程及成果）
  </h3>
  <el-upload
  :action="request_url"
  list-type="picture-card"
  :headers="set_headers2"
  :on-preview="handlePictureCardPreview"
  :beforeUpload="beforeUpload1"
  :on-success="show_success"
  :on-remove="handleRemove">
   
  <i class="el-icon-plus"></i>
</el-upload>
<el-dialog :visible.sync="dialogVisible">
  <img width="100%" :src="dialogImageUrl" alt="">
</el-dialog>

  </div>
</template>

<script>
import {Message} from 'element-ui'
export default {
    data() {
      return {
        fileList: []
        ,dialogImageUrl: '',
        request_url: this.$store.state.back_url + '/upload/subject_name/dirname', 
        dialogVisible: false,
        disabled: false,
        set_headers1:  {
          token: localStorage.getItem('token'),
          subject_name: encodeURIComponent(localStorage.getItem('subject_name')),
          dirname: encodeURIComponent("特色活动方案")
        },
        set_headers2:  {
          token: localStorage.getItem('token'),
          subject_name: encodeURIComponent(localStorage.getItem('subject_name')),
          dirname: encodeURIComponent("特色活动图片")
        }
      };
    },
    methods: {
      submitUpload() {
        this.$refs.upload.submit();
      },
      handlePreview(file) {
        console.log(file);
      },
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      },
      handleDownload(file) {
        console.log(file);
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
    },
    show_success(){
      this.$message.success('上传成功')
    },
    beforeUpload1(file) {
      const isJPG = file.type === "image/jpeg";
      const isLt2M = file.size / 1024 / 1024 < 10;

      if (!isJPG) {
        alert("上传头像图片只能是 JPG 格式!");
        this.$message.error("上传头像图片只能是 JPG 格式!");
      }
      if (!isLt2M) {
        alert(this.$message.error("上传头像图片大小不能超过 10MB!"));
        this.$message.error("上传头像图片大小不能超过 10MsB!");
      }
      return isJPG && isLt2M;
    },
  },
    }

</script>

<style>

</style>