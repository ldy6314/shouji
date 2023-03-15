<template>
  <div id="login">
    <b-row>
     
      <b-col cols="6" offset="3">
        <div id='in-login'>
           <h5 class="text-center">请登录</h5>
           <hr>
          <b-form>
            <b-form-group label="账户" label-for="name-input">
              <b-form-input
                id="name-input"
                placeholder="请输入账号"
                required
                v-model="form.account"
              >
              </b-form-input>
            </b-form-group>
            <b-form-group label="密码" label-for="pwd-input">
              <b-form-input
                id="pwd-input"
                placeholder="请输入密码"
                type="password"
                required
                v-model="form.pwd"
              >
              </b-form-input>
            </b-form-group>
            <b-form-group>
              <b-form-checkbox> 记住我 </b-form-checkbox>
            </b-form-group>
          </b-form>
          <b-button variant="info" @click="submit">登录</b-button>
        </div>
      </b-col>
    </b-row>
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