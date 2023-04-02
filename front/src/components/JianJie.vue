<template>
  <div>
    <h3>教师风采</h3>
    <el-upload
      class="avatar-uploader"
      action="http://127.0.0.1:5000/upload/subject_name/dirname"
      :show-file-list="false"
      :on-success="handleAvatarSuccess"
      :before-upload="beforeAvatarUpload"
      :headers="set_headers"
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
        <el-button type="primary" @click="add_subject_info">提交</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import _axios from '@/utils/_axios';
import { Message } from 'element-ui';
export default {
  data() {
    return {
      textarea: "",
      textarea2: " ",
      imageUrl: "",
       set_headers:  {
          token: localStorage.getItem('token'),
          subject_name: encodeURIComponent(localStorage.getItem('subject_name')),
          dirname: encodeURIComponent("教师风采")
        }
    };
  },
  methods: {
    handleAvatarSuccess(res, file) {
      alert(2);
      this.imageUrl = URL.createObjectURL(file.raw);
    },
    add_subject_info(){
      let formData =new FormData()
      formData.append('teacher_info', this.textarea)
      formData.append('subject_info', this.textarea2)
      formData.append('subject_name',localStorage.getItem('subject_name'))
      _axios.post('http://127.0.0.1:5000/add_subject_info',formData
      ).then(
        success=>{
          Message({
            message:success,
            type:'success'
          })
        },
        error=>{
          console.log(error)
        }
      )
    }
    ,
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