<template>
  <div>
    <h3>批量上传账号</h3>
    <el-upload
      class="upload-demo"
      ref="upload"
      :action="request_url"
      :on-preview="handlePreview"
      :on-remove="handleRemove"
      :file-list="fileList"
      :auto-upload="false"
      :on-success="show_success"
      :before-upload="beforeUpload"
    >
      <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
      <el-button
        style="margin-left: 10px"
        size="small"
        type="success"
        @click="submitUpload"
        >上传到服务器</el-button
      >
      <div slot="tip" class="el-upload__tip">
        只能上传.xlsx文件
      </div>
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
        <el-input
          v-model="formInline.subject_name"
          placeholder="账户名称"
        ></el-input>
      </el-form-item>
      <el-form-item label="角色">
        <el-select v-model="formInline.role" placeholder="角色">
          <el-option label="管理员" value="0"></el-option>
          <el-option label="社团教师" value="1"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">添加</el-button>
      </el-form-item>
    </el-form>
    <h3>账户信息</h3>
    <el-table :data="userlist" style="width: 100%">
      <el-table-column label="序号" width="180">
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{ scope.$index + 1 }}</span>
        </template>
      </el-table-column>
      <el-table-column label="社团名称" width="180">
        <template slot-scope="scope">
          <span>{{ scope.row.subject_name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="社团账号" width="180">
        <template slot-scope="scope">
          <span>{{ scope.row.username }}</span>
        </template>
      </el-table-column>
      <el-table-column label="教师姓名" width="180">
        <template slot-scope="scope">
          <span>{{ scope.row.teacher_name }}</span>
        </template>
      </el-table-column>

      <el-table-column label="权限" width="180">
        <template slot-scope="scope">
          <span>{{ scope.row.role == 0 ? "管理员" : "社团教师" }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            type="primary"
            size="mini"
            @click="resetPassword(scope.row.username)"
            >重置密码</el-button
          >
          <el-button
            type="danger"
            size="mini"
            @click="removeUser(scope.row.username)"
            >删除</el-button
          >
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import _axios from "@/utils/_axios";
import { Message } from "element-ui";
export default {
  inject:['reload'],
  data() {
    return {
      request_url: this.$store.state.back_url + '/upload_users', 
      fileList: [],
      formInline: {
        user: "",
        pwd: "",
        subject_name: "",
        name: "",
        role: "社团教师",
      },
      userlist: [],
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
    beforeUpload(file)
    {
       if(file.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
           return true
        Message({
          message: "只能选择.xlsx文件",
          type:"warning"
        })
        return false
    },
    show_success(res)
    {
        console.log(res)
        Message({
        
          message:"上传成功",
          type: "success"
        })
        this.reload()
    },
    resetPassword(username) {
      if (username == "admin") return;
      if (confirm("确定要重置密码？")) {
        let data = { username: username };
        _axios.post("reset_password", data).then(
          (success) => {
            success;
            alert("密码已经重置为88888888");
          },
          (error) => {
            error;
          }
        );
      }
    },
    removeUser(username) {
      if (confirm(`确认要删除用户${username}一次`)) {
        if (confirm(`确认要删除用户${username}两次`)) {
          if (confirm(`确认要删除用户${username}三次`)) {
            let data = { username: username };
            _axios.post("http://127.0.0.1:5000/remove_user", data).then(
              (success) => {
                Message({
                    message:success.message,
                    type:"success"
                })
                this.reload()
              },
              (error) => {
                Message({
                    message:error.respone.message,
                    type:"error"
                })
              }
            );
          }
        }
      }
    },
    onSubmit() {
      _axios.post("http://127.0.0.1:5000/add_user", this.formInline).then(
        (success) => {
          Message({ message: success , type:"success"});
          this.reload()
        },
        (err) => {
          Message({ message: err.message });
        }
      );
    },
  },
  mounted() {
    _axios.get("/get_userlist").then(
      (success) => {
        this.userlist = success;
      },
      (err) => {
        console.log(err);
      }
    );
  },
};
</script>

<style>
</style>