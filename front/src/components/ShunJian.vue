<template>
  <div>
    <h3>上传照片</h3>
    <el-upload
  action="http://127.0.0.1:5000/upload/subject_name/dirname"
  list-type="picture-card"
  :on-preview="handlePictureCardPreview"
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

    }
  }
</script>