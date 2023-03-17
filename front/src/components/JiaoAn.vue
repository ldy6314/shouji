<template>
  <div id='jiaoan'>
     <b-card title="课时教案"> 
      <b-form-file v-model="file1" class="mt-3" plain></b-form-file>
       <div class="mt-3">教案1: {{ file1 ? file1.name : '' }}</div>
        
        <b-form-file v-model="file2" class="mt-3" plain></b-form-file>
       <div class="mt-3">教案2: {{ file2 ? file2.name : '' }}</div>
        
        <b-form-file v-model="file3" class="mt-3" plain></b-form-file>
       <div class="mt-3">教案3: {{ file3 ? file3.name : '' }}</div>
        
        <b-form-file v-model="file4" class="mt-3" plain></b-form-file>
       <div class="mt-3">教案4: {{ file4 ? file4.name : '' }}</div>
        
        <b-form-file v-model="file5" class="mt-3" plain></b-form-file>
       <div class="mt-3">教案5: {{ file5 ? file5.name : '' }}</div>
        
        <b-form-file v-model="file6" class="mt-3" plain></b-form-file>
       <div class="mt-3">教案6: {{ file6 ? file6.name : '' }}</div>
        
        <b-form-file v-model="file7" class="mt-3" plain></b-form-file>
       <div class="mt-3">教案7: {{ file7 ? file7.name : '' }}</div>
        
        <b-form-file v-model="file8" class="mt-3" plain></b-form-file>
       <div class="mt-3">教案8: {{ file8 ? file8.name : '' }}</div>
        
        <b-form-file v-model="file9" class="mt-3" plain></b-form-file>
       <div class="mt-3">教案9: {{ file9 ? file9.name : '' }}</div>
        
        <b-form-file v-model="file10" class="mt-3" plain></b-form-file>
       <div class="mt-3">教案10: {{ file10 ? file10.name : '' }}</div>
        
        <b-form-file v-model="file11" class="mt-3" plain></b-form-file>
       <div class="mt-3">教案11: {{ file11 ? file11.name : '' }}</div>
        
        <b-form-file v-model="file12" class="mt-3" plain></b-form-file>
       <div class="mt-3">教案12: {{ file12 ? file12.name : '' }}</div>
     </b-card>
   
  </div>
</template>

<script>
export default {
   data(){
    return {
       file1:null,
       file2:null,
       file3:null,
       file4:null,
       file5:null,
       file6:null,
       file7:null,
       file8:null,
       file9:null,
       file10:null,
       file11:null,
       file12:null,
    }
   },
}
</script>

<style>

</style>