<template>
    <div id="zongjie">
     <b-card
        title="教学总结">
     <b-form-file
       v-model="file1"
       :state="Boolean(file1)"
       placeholder="从这里选择文件"
       drop-placeholder="从这里删除文件"
     ></b-form-file>
     <div class="mt-3">已选择文件: {{ file1 ? file1.name : '' }}</div>
     <b-button variant="info">
       上传
     </b-button>
     </b-card>
     
   </div>
  </template>
  
  <script>
  export default {
   data() {
       return {
         file1: null
       }
     }
  }
  </script>
  
  <style>