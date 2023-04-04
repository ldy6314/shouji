<template>
  <div>
    <h3>上传照片</h3>
    <el-upload
  :action="request_url"
  list-type="picture-card"
  :on-preview="handlePictureCardPreview"
  :before-upload="beforeUpload1"
  :headers="set_headers"
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
        dialogImageUrl: '',
        request_url: this.$store.state.back_url + '/upload/subject_name/dirname', 

        dialogVisible: false,
        set_headers:  {
          token: localStorage.getItem('token'),
          subject_name: encodeURIComponent(localStorage.getItem('subject_name')),
          dirname: encodeURIComponent("精彩瞬间")
        }
      };
    },
    methods: {
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      },
      beforeUpload1(file) {
      const isJPG = file.type === "image/jpeg";
      const isLt2M = file.size / 1024 / 1024 < 10;

      if (!isJPG) {
        this.$message.error("上传头像图片只能是 JPG 格式!");
      }
      if (!isLt2M) {
        this.$message.error("上传头像图片大小不能超过 10MsB!");
      }
      return isJPG && isLt2M;
    },
    }
  }
</script>