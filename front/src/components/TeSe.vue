<template>
  <div>
    
   <h3>
    特色活动方案
   </h3>
   <el-upload
  class="upload-demo"
  ref="upload"
  action="http://127.0.0.1:5000/upload/subject_name/dirname"
  :on-preview="handlePreview"
  :on-remove="handleRemove"
  :file-list="fileList"
  :headers="set_headers1"
  :auto-upload="false">
  <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
  <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
  <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>

</el-upload>
  <h3>
    特色活动照片（过程及成果）
  </h3>
  <el-upload
  action="http://127.0.0.1:5000/upload/subject_name/dirname"
  list-type="picture-card"
  :headers="set_headers2"
  :on-preview="handlePictureCardPreview"
  :on-remove="handleRemove">
   
  <i class="el-icon-plus"></i>
</el-upload>
<el-dialog :visible.sync="dialogVisible">
  <img width="100%" :src="dialogImageUrl" alt="">
</el-dialog>

  </div>
</template>

<script>
export default {
    data() {
      return {
        fileList: []
        ,dialogImageUrl: '',
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
      }
    }
  }
</script>

<style>

</style>