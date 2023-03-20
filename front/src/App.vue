<template>
  <div id="app">
      <el-row>
        <el-col :span = "24">
        <el-menu
    :router="true"
  :default-active="activeIndex2"
  class="el-menu-demo"
  mode="horizontal"
  @select="handleSelect"
  background-color="#545c64"
  text-color="#fff"
  active-text-color="#ffd04b">
  <el-menu-item index="/gailan">社团概览</el-menu-item>
  <el-menu-item index="/jianjie">社团简介</el-menu-item>
  <el-menu-item index="/jihua" >社团计划</el-menu-item>
   <el-menu-item index="/jiaoan" >课时教案</el-menu-item>
   <el-menu-item index="/zongjie" >社团总结</el-menu-item>
   <el-menu-item index="/shunjian" >精彩瞬间</el-menu-item>
   <el-menu-item index="/tese" >特色活动</el-menu-item>
    <el-menu-item index="/login"  class="login">登录</el-menu-item>
</el-menu>
</el-col>
</el-row>
<el-row>
  <router-view>
  显示区
</router-view>
</el-row>

  </div>
</template>
<script>
   export default {
    data() {
      return {
        activeIndex2: '1'
      };
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
</script>
<style scoped>
     .login{
      float: right;
      margin-right: 50px ;
     }
</style>
