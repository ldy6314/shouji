<template>
  <div>
    <h3>批量上传账号</h3>
    <el-upload
  class="upload-demo"
  ref="upload"
  action="https://jsonplaceholder.typicode.com/posts/"
  :on-preview="handlePreview"
  :on-remove="handleRemove"
  :file-list="fileList"
  :auto-upload="false">
  <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
  <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
  <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
</el-upload>
<h3>添加单个账户</h3>
<el-form :inline="true" :model="formInline" class="demo-form-inline">
  <el-form-item label="账户名">
    <el-input v-model="formInline.user" placeholder="用户名"></el-input>
  </el-form-item>
  <el-form-item label="密码">
    <el-input v-model="formInline.pwd" placeholder="密码"></el-input>
  </el-form-item>
  <el-form-item label="姓名">
    <el-input v-model="formInline.name" placeholder="密码"></el-input>
  </el-form-item>
  <el-form-item label="社团名称">
    <el-input v-model="formInline.subject_name" placeholder="账户名称"></el-input>
  </el-form-item>
  <el-form-item label="角色">
    <el-select v-model="formInline.role" placeholder="角色">
      <el-option label="管理员" value=0></el-option>
      <el-option label="社团教师" value=1></el-option>
    </el-select>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="onSubmit">添加</el-button>
  </el-form-item>
</el-form>
  </div>
</template>

<script>
 export default {
    data() {
      return {
           fileList : [],
           formInline:{
            user:"",
            pwd:"",
            subject_name: "",
            name:"", 
            role: "社团教师"
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
      onSubmit() {
        console.log(this.formInline)
      }
    }
  }
</script>

<style>

</style>