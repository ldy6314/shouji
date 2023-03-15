<template>
  <div id="app">
    <b-container>
    <b-navbar toggleable="lg" type="dark" variant="info" id='nav-bar'>
      <b-navbar-brand href="#">俱乐部资料</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item to="/">首页</b-nav-item>
          <b-nav-item to="/myword">资料上传</b-nav-item>
          <b-nav-item to="/myword">资料管理</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">
          <b-nav-item to="/regist">注册</b-nav-item>
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
