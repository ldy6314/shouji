<template>
  <div id="app">
    <b-container>
    <b-navbar toggleable="lg" type="dark" variant="info" id='nav-bar'>
      <b-navbar-brand href="#">俱乐部资料</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/gailan">概览</b-nav-item>
          <b-nav-item to="/jianjie">课程简介</b-nav-item>
          <b-nav-item to="/jihua">教学计划</b-nav-item>
          <b-nav-item to="/jiaoan">课时教案</b-nav-item>
          <b-nav-item to="/zongjie">教学总结</b-nav-item>
          <b-nav-item to="/tese">特色活动</b-nav-item>
          <b-nav-item to="/shunjian">精彩瞬间</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <!-- <b-nav-item to="/regist">注册</b-nav-item> -->
          <b-nav-item to="/login">登录</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>

    <router-view></router-view>
    </b-container>
  </div>
</template>

<style>
</style>
