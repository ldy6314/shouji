<template>
  <div>
       {{tabaleData}}
      <ul>
          <li v-for="(idx,item) in tabaleData" :key="item">
            {{item}}{{idx}}
              </li>
      </ul>
     

    
   </div>
</template>

<script>
import _axios from '@/utils/_axios'

export default {
data(){
   return{
      tabaleData:[]
   }   
},
mounted(){
   _axios.get('get_admin_infos').then(
      success=>{
         this.tabaleData = success
         let data = success
         for(let d of data){
            let sub_name = d.subject_name
            let content = d.content
            content.name = sub_name
            console.log(content)
         }
      },
      err=>{
         console.log(err)
      }
   )
}
 
}
</script>

<style>

</style>