<template>
  <div id='regist'>
    <b-row>
      <b-col cols="6" offset="3">
    <div id='in-regist'>
       <h5 class="text-center">账号注册</h5>
           <hr>
      <b-form>
        <b-form-group label="邮箱" label-for="name-input">
          <b-form-input
            id="name-input"
            placeholder="请输入邮箱地址作为账号"
            required
            v-model="form.email"
          >
          </b-form-input>
        </b-form-group>
         <b-form-group label="昵称" label-for="nick-input">
          <b-form-input
            id="nick-input"
            placeholder="输入一个昵称"
            required
            v-model="form.nick"
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
     <b-form-group label="确认密码" label-for="confirm-pwd-input">
          <b-form-input
            id="confirm-pwd-input"
            placeholder="请输入相同的密码"
            type="password"
            required
            v-model="form.cofirm_pwd"
          >
          </b-form-input>
        </b-form-group>
        
      <b-button variant="info" @click="submit">注册</b-button>
      </b-form>
    </div>
    </b-col>
    </b-row>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      form: {
        email: "",
        pwd: "",
        confirm_pwd:"",
        nick: ""
      },
    };
  },
  methods:{
    submit(){
      axios.post('http://localhost:8888/sign_up',
      {
        form:this.form
      }
      ).then((res)=>{
        console.log(res)
      }
      ).catch((err)=>{
        console.log(err)
      })
    }
  }
};
</script>

<style>
#in-regist {
  
  padding: 20px;
  border: solid;
  border-color:rgb(208, 215, 215) ;
  border-radius: 5px;
}
</style>