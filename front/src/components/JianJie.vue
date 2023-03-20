<template>
  <div>
    <el-row>
      <el-col :span="6" offset="3">
        <el-card header="头像">
          <el-upload
            class="avatar-uploader"
            action="https://jsonplaceholder.typicode.com/posts/"
            :show-file-list="false"
            :on-success="handleAvatarSuccess"
            :before-upload="beforeAvatarUpload"
          >
            <img v-if="imageUrl" :src="imageUrl" class="avatar" />
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>
        </el-card>
      </el-col>
      <el-col :span="6">
        <el-card header="教师简介">
          <el-input
            type="textarea"
            :rows="8"
            placeholder="请输入内容"
            v-model="textarea"
          >
          </el-input>
        </el-card>
      </el-col>
       <el-col :span="6">
        <el-card header="社团简介">
          <el-input
            type="textarea"
            :rows="8"
            placeholder="请输入内容"
            v-model="textarea2"
          >
          </el-input>
        </el-card>
      </el-col>
     
    </el-row>
    <el-row>
      <el-col :span="1" offset="11">
        <el-button>提交</el-button>
      </el-col>
    </el-row>
 
  </div>
</template>

<script>
export default {
  textarea:"",
  textarea2:""
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
.el-card{
  height: 300px;
}
</style>