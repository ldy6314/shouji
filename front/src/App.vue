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
          <el-menu-item index="/" v-if="role==1"
            ><span style="font-size: 20px">社团概览</span></el-menu-item
          >
          <el-menu-item index="/adminhome" v-if="role==0"
            ><span style="font-size: 20px">管理首页</span></el-menu-item
          >
      
          <el-menu-item index="/account" v-if="role==0"
            ><span style="font-size: 20px">账户管理</span></el-menu-item
          >
          <el-menu-item index="/jianjie" v-if="role==1"
            ><span style="font-size: 20px">社团简介</span></el-menu-item
          >
          <el-menu-item index="/jihua" v-if="role==1"
            ><span style="font-size: 20px">社团计划</span></el-menu-item
          >
          <el-menu-item index="/jiaoan" v-if="role==1"
            ><span style="font-size: 20px">课时教案</span></el-menu-item
          >
          <el-menu-item index="/zongjie" v-if="role==1"
            ><span style="font-size: 20px">社团总结</span></el-menu-item
          >
          <el-menu-item index="/shunjian" v-if="role==1"
            ><span style="font-size: 20px">精彩瞬间</span></el-menu-item
          >
          <el-menu-item index="/tese" v-if="role==1"
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
      <router-view v-if="isRouterAlive"> 显示区 </router-view>
    </el-row>
  </div>
</template>
<script>
import router from './router';
export default {
  data() {
    return {
      activeIndex2: "1",
      isRouterAlive: true,
    };
  },
  provide(){
    return {
      reload: this.reload
    }
  }
  ,
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    logout(){
        localStorage.clear()
        this.logined = false
        this.$store.commit('LOGIN', {token:""})
        router.push('/login')
    },
    reload(){
      this.isRouterAlive = false
      this.$nextTick(function(){
        this.isRouterAlive = true
      })
    }
  },
  computed:{
   role(){
    return this.$store.state.role
   },
   logined:{
    get(){
    return this.$store.state.logined
   }, 
   set(val){
    this.$store.state.logined = val
   }
   }

  },
  mounted(){
    let token = localStorage.getItem('token')
    let role = localStorage.getItem('role')
    this.$store.commit('LOGIN', {token:token, role:role})
    if(role==0)
      router.replace('/adminhome') 
    if(this.$store.state.logind == false)
      router.replace('/login')
  }
}
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
