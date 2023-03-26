<template>
  <div id="app">
    <el-row id="header">
      <el-col :span="24">
        <div >合肥市锦城小学社团资料收集平台</div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="24">
        <el-menu
          :router="true"
          :default-active="activeIndex2"
          class="el-menu-demo"
          mode="horizontal"
          @select="handleSelect"
          background-color="#2E8B57"
          text-color="#fff"
          active-text-color="#ffd04b"
        >
          <el-menu-item index="/"
            ><span style="font-size: 20px">社团概览</span></el-menu-item
          >
          <el-menu-item index="/jianjie"
            ><span style="font-size: 20px">社团简介</span></el-menu-item
          >
          <el-menu-item index="/jihua"
            ><span style="font-size: 20px">社团计划</span></el-menu-item
          >
          <el-menu-item index="/jiaoan"
            ><span style="font-size: 20px">课时教案</span></el-menu-item
          >
          <el-menu-item index="/zongjie"
            ><span style="font-size: 20px">社团总结</span></el-menu-item
          >
          <el-menu-item index="/shunjian"
            ><span style="font-size: 20px">精彩瞬间</span></el-menu-item
          >
          <el-menu-item index="/tese"
            ><span style="font-size: 20px">特色活动</span></el-menu-item
          >
          <el-menu-item  v-if="!logined" index="/login" class="login"
            ><span style="font-size: 20px">登录</span></el-menu-item
          >
          
         <el-menu-item  v-if="logined" class="login"><span  style="font-size: 20px" @click="logout">退出登录</span></el-menu-item> 
        </el-menu>
      </el-col>
    </el-row>
    <el-row>
      <router-view> 显示区 </router-view>
    </el-row>
  </div>
</template>
<script>
import router from './router';
export default {
  data() {
    return {
      activeIndex2: "1",
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    logout(){
        localStorage.clear()
        this.logined = false
        this.$store.commit('LOGIN', {token:""})
        router.push('/login')
    }
  },
  computed:{
    logined(){
      let token = this.$store.state.token
      if(token!="")
        return true
      else 
         return false
    }
  },
  mounted(){
    
    console.log(111111111111111111,this.$store.state.token)

  }
};
</script>
<style scoped>
.login {
  float: right;
  margin-right: 20px;
  color: white;
}
h2 {
  text-align: center;
}
#header {
  height: 50px;
  font-size:30px;
  background-color: 	#2E8B57;
  text-align: center;
  color:white
}

</style>
