<template>
  <div id="login">
    <el-row>
      <el-col span="12" offset="6">
    
           
      </el-col>
    </el-row>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      form: {
        account: "",
        pwd: "",
      },
    };
  },
  methods: {
    submit() {
      axios
        .post("http://localhost:8888/login", {
          account: this.form.account,
          pwd: this.form.pwd,
        })
        .then((res) => {
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
#in-login {
  margin-top: 10px;
  padding: 20px;
  border: solid;
  border-color:rgb(208, 215, 215) ;
  border-radius: 1px;
}
</style>