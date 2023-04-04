<template>
  <div>
   <el-table
    :data="tableData"
    style="width: 100%">
    <el-table-column
      fixed
      prop="subject_name"
      label="项目名称"
      >
    </el-table-column>
    <el-table-column
      prop="teacher_name"
      label="教师姓名"
   >
    </el-table-column>
    <el-table-column
      prop="fengcai"
      label="教师照片"
   >
    </el-table-column>
    <el-table-column
      prop="jihua"
      label="社团计划"
   >
    </el-table-column>
    <el-table-column
      prop="tese"
      label="特色方案"
>
    </el-table-column>
    <el-table-column
      prop="tesetp"
      label="特色方案图片">
    </el-table-column>
    <el-table-column
      prop="zongjie"
      label="总结">
    </el-table-column>
    <el-table-column
      prop="shunjian"
      label="瞬间图片">
    </el-table-column>
    <el-table-column
      fixed="right"
      label="操作">
      <template slot-scope="scope">
        <el-button @click="handleClick(scope.row)" type="text" size="small">查看</el-button>
      </template>
    </el-table-column>
  </el-table>

    
   </div>
</template>

<script>
import _axios from '@/utils/_axios'

export default {
data(){
   return{
      tableData:[]
   }   
},
methods:{
  handleClick(row){
    alert(row.subject_name,"功能建设中，敬请期待" )
  }
},
mounted(){
   _axios.get('get_admin_infos').then(
      success=>{
         this. tableData= success
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