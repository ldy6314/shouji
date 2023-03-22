<template>
  <div>
    <h3>教师风采</h3>
    <el-upload
      class="avatar-uploader"
      action="http://127.0.0.1:5000/upload_pic"
      :show-file-list="false"
      :on-success="handleAvatarSuccess"
      :before-upload="beforeAvatarUpload"
    >
      <img v-if="imageUrl" :src="imageUrl" class="avatar" />
      <i v-else class="el-icon-plus avatar-uploader-icon"></i>
    </el-upload>
    <h3>教师介绍</h3>
    <el-row>
      <el-col :span="12">
        <el-input
      type="textarea"
      :rows="5"
      v-model="textarea"
    >
    </el-input>
      </el-col>
    </el-row>
    <h3>社团介绍</h3>
    <el-row>
      <el-col :span="12">
        <el-input
      type="textarea"
      :rows="5"
      v-model="textarea2"
    >
    </el-input>
      </el-col>
    </el-row>
    
 
    
    <el-row>
      <br>
      <el-col :span="1">
        <el-button type="primary">提交</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      textarea: "",
      textarea2: " ",
      imageUrl: "",
    };
  },
  methods: {
    handleAvatarSuccess(res, file) {
      alert(2);
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    beforeAvatarUpload(file) {
      const isJPG = file.type === "image/jpeg";
      const isLt2M = file.size / 1024 / 1024 < 10;

      if (!isJPG) {
        alert("上传头像图片只能是 JPG 格式!");
        this.$message.error("上传头像图片只能是 JPG 格式!");
      }
      if (!isLt2M) {
        alert(this.$message.error("上传头像图片大小不能超过 10MB!"));
        this.$message.error("上传头像图片大小不能超过 2MsB!");
      }
      return isJPG && isLt2M;
    },
  },
};
</script>
<style>
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}
.avatar-uploader .el-upload:hover {
  border-color: #409eff;
}
.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 178px;
  height: 178px;
  line-height: 178px;
  text-align: center;
}
.avatar {
  width: 178px;
  height: 178px;
  display: block;
}
.el-card {
  height: 300px;
  margin-top: 20px;
  margin-bottom: 20px;
}
</style>