<template>
  <div id="gailan">
    <h3>{{ subject_name }}</h3>
    <h3>社团介绍</h3>
    <p>
      {{subject_info}}
    </p>
    <h3>教师风采</h3>
    <el-image :src="tx_url" style="width: 400px"> </el-image>
    <h3>教师简介</h3>
    <p>
      {{teacher_info}}
    </p>
    <h3>文字资料</h3>
    <el-table :data="tableData" style="width: 100%">
      <el-table-column label="资料名称" width="180">
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{ scope.row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="文件名" width="180">
        <template slot-scope="scope">
          <span>{{ scope.row.filename }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <i class="el-icon-download"  type="primary"
            @click="handleEdit(scope.$index, scope.row)"></i>
            <i class="el-icon-delete"  @click="handleDelete(scope.$index, scope.row)"></i>
        </template>
      </el-table-column>
    </el-table>
    <h3>社团教案</h3>
    <el-table :data="tableData2" style="width: 100%">
      <el-table-column label="序号" width="180">
        <template slot-scope="scope">
          <span style="margin-left: 10px">{{ scope.$index + 1 }}</span>
        </template>
      </el-table-column>
      <el-table-column label="文件名" width="180">
        <template slot-scope="scope">
          <span>{{ scope.row.name }}</span>
        </template>
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <i class="el-icon-edit"  type="primary"
            @click="handleEdit(scope.$index, scope.row)"></i>
            <i class="el-icon-delete"  @click="removeimage(scope.row.name)"></i>
        </template>
      </el-table-column>
    </el-table>
    <h3>精彩瞬间图片</h3>
    <el-row>
      <el-col :span="3" v-for="(item, index) in shunjian_list" :key="index">
        <div class="el-card-define">
          <el-image
            :src="item"
            style="width: 100%; margin-left: 5px"
          ></el-image>
          <div class="btdiv">
            <i class="el-icon-download" @click="download_pic(item)"></i>
            <i class="el-icon-delete" @click="removeimage(item)"></i>
          </div>
        </div>
      </el-col>
    </el-row>

    <h3>特色活动图片</h3>
    <el-row>
      <el-col :span="3" v-for="(item, index) in tese_list" :key="index">
        <div class="el-card-define">
          <el-image
            :src="item"
            style="width: 100%; margin-left: 5px"
          ></el-image>
          <div class="btdiv">
            <i class="el-icon-download" @click="download_pic(item)"></i>
            <i class="el-icon-delete" @click="removeimage(item)"></i>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import _axios from '@/utils/_axios';
import { Message } from 'element-ui';
export default {
  inject: ['reload'],
  data() {
    return {
      backend_url: "http://127.0.0.1:5000/get_img/",
      subject_name: "",
      shunjian_list: [],
      tese_list:[],
      tableData: [],
      tableData2: [],
      tx_url: "",
      subject_info: "",
      teacher_info:""
    };
  },
  methods: {
    handleEdit(index, row) {
      console.log(index, row);
    },
    handleDelete(index, row) {
      console.log(index, row);
    },
    removeimage(item) {
      console.log(item)
      let a = item.split("/");
      console.log(a)
      let image_name = a[a.length-1]
      let dir = a[a.length-3]
      let dir_name=""
      if(dir == "get_sj")
        dir_name = "精彩瞬间"
      else  if(dir=="get_ts")
        dir_name = "特色活动图片" 
      else
         dir_name ="课时教案"
      let data ={
        subject_name:this.subject_name,
        dir_name:dir_name ,
        image_name:image_name
      }
      _axios.post('remove_resource', data).then(
        success=>{
          success
          Message({
            message:"删除成功",
            type: "success"
          })
          this.reload()
        },
        err=>{
          Message({message:err.response.message,
          type: "danger"
        })
        }
      )
    },
    download_pic(item) {
      alert(item);
    },
  },

  mounted() {
    let data={
      subject_name: localStorage.getItem('subject_name'),
      back_url: this.$store.state.back_url
    }
    this.subject_name = data.subject_name
    _axios.post("get_userinfos", data).then(
      success=>{
        this.tx_url = data.back_url + '/get_tx/'+encodeURIComponent(data.subject_name)+'/'+success.tx
        this.subject_info = success.subject_info
        this.teacher_info = success.teacher_info
        for(let pic of success.shunjian)
        {
         
          this.shunjian_list.push( data.back_url + '/get_sj/'+encodeURIComponent(data.subject_name)+'/'+pic)
        }
        for(let pic of success.tesetupian)
        {
          this.tese_list.push( data.back_url + '/get_ts/'+encodeURIComponent(data.subject_name)+'/'+pic)
        }
        for(let ja of success.jiaoan){
          this.tableData2.push({
            name:ja
          })
        }

        let  a =[
          {
            name: "计划",
            filename:success.jihua[0] || "未上传"
          },
          {
            name:"总结",
            filename:success.zongjie[0]|| "未上传"
          },
          {
            name:"特色活动方案",
            filename:success.tesefa[0] || "未上传" 
          }
        ]

         success.tesefa[0]
        for(let ja of a){
           this.tableData.push(ja)
        }


      },
      err=>{
        console.log(err)
      }
    )
  },
};
</script>

<style scoped>
.img {
  height: 200px;
}
.el-card-define {
  position: relative;
  min-height: 100%;
  height: 100%;
}
.el-card-define:hover {
  background-color: darkgray;
  opacity: 50%;
}
.el-card-define:hover .btdiv {
  display: block;
}
.btdiv {
  display: none;
  text-align: center;
  position: absolute;
  left: 40%;
  top: 30%;
}
i{
  font-size: 30px
}
.btdiv i{
  color:black;
}
</style>