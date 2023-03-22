<template>
  <div id="gailan">
    <h3>社团介绍</h3>
    <p></p>
    <h3>教师风采</h3>
    <el-img> </el-img>
    <p>
      教师介绍..............................................................................
    </p>
    <h3>文字资料</h3>
    <el-table
    :data="tableData"
    style="width: 100%">
    <el-table-column
      label="资料名称"
      width="180">
      <template slot-scope="scope">
        <span style="margin-left: 10px">{{ scope.row.name }}</span>
      </template>
    </el-table-column>
    <el-table-column
      label="文件名"
      width="180">
      <template slot-scope="scope">
          <span>{{scope.row.filename}}</span>
      </template>
    </el-table-column>
    <el-table-column label="操作">
      <template slot-scope="scope">
        <el-button
          size="mini"
          type="primary"
          @click="handleEdit(scope.$index, scope.row)">下载</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
  <h3>社团教案</h3>
    <el-table
    :data="tableData2"
    style="width: 100%">
    <el-table-column
      label="序号"
      width="180">
      <template slot-scope="scope">
        <span style="margin-left: 10px">{{ scope.$index + 1 }}</span>
      </template>
    </el-table-column>
    <el-table-column
      label="文件名"
      width="180">
      <template slot-scope="scope">
          <span>{{scope.row.name}}</span>
      </template>
    </el-table-column>
    <el-table-column label="操作">
      <template slot-scope="scope">
        <el-button
          size="mini"
          type="primary"
          @click="handleEdit(scope.$index, scope.row)">下载</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
    </el-table-column>
  </el-table>
  
  </div>
</template>

<script>
  export default {
    data() {
      return {
        tableData: [{
         name: '社团计划',
          filename: '社团计划.docx',
         
        }, {
          name: '社团总结',
          filename: '社团总结.docx',
        }, {
          name: '社团特色活动方案',
          filename: '社团特色活动方案.docx',
        }, ],
        tableData2:[
          {
            name: '第1课时教案.docx'
          },
          {
            name: '第2课时教案.docx'
          },
          {
            name: '第3课时教案.docx'
          },
          {
            name: '第4课时教案.docx'
          },
          {
            name: '第5课时教案.docx'
          },
          {
            name: '第6课时教案.docx'
          },
          {
            name: '第7课时教案.docx'
          },
          {
            name: '第8课时教案.docx'
          },
          {
            name: '第9课时教案.docx'
          },
          {
            name: '第10课时教案.docx'
          },
          {
            name: '第11课时教案.docx'
          },
          {
            name: '第12课时教案.docx'
          }      
        ]
      }
    },
    methods: {
      handleEdit(index, row) {
        console.log(index, row);
      },
      handleDelete(index, row) {
        console.log(index, row);
      }
    }
  }
</script>

<style>
</style>