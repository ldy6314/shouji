<template>
  <div id="gailan">
    <h3>{{ subject_name }}</h3>
    <h3>社团介绍</h3>
    <p>
      {{subject_info}}
    </p>
    <h3>教师风采</h3>
    <el-image :src="tx_url" style="width: 400px"> </el-image>
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
          <!-- <el-button
            size="mini"
            type="primary"
            @click="handleEdit(scope.$index, scope.row)"
            >下载</el-button
          >
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)"
            >删除</el-button
          > -->
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
          <!-- <el-button
            size="mini"
            type="primary"
            @click="handleEdit(scope.$index, scope.row)"
            >下载</el-button
          >
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)"
            >删除</el-button
          > -->
          <i class="el-icon-download"  type="primary"
            @click="handleEdit(scope.$index, scope.row)"></i>
            <i class="el-icon-delete"  @click="handleDelete(scope.$index, scope.row)"></i>
        </template>
      </el-table-column>
    </el-table>
    <h3>精彩瞬间图片</h3>

    <!-- <el-card>
      <el-image
      v-for="(item, index) in imglist"
      :key="index"
      :src="item"
      style="width: 100px; margin-left: 5px"
    >
    </el-image>
  </el-card> -->
    <el-row>
      <el-col :span="3" v-for="(item, index) in imglist" :key="index">
        <div class="el-card-define">
          <el-image
            :src="item"
            style="width: 100%; margin-left: 5px"
          ></el-image>
          <div class="btdiv">
            <i class="el-icon-download" @click="download_pic(item)"></i>
            <i class="el-icon-delete"></i>
          </div>
        </div>
      </el-col>
    </el-row>

    <h3>特色活动图片</h3>
    <el-row>
      <el-col :span="3" v-for="(item, index) in imglist" :key="index">
        <div class="el-card-define">
          <el-image
            :src="item"
            style="width: 100%; margin-left: 5px"
          ></el-image>
          <div class="btdiv">
            <i class="el-icon-download" @click="download_pic(item)"></i>
            <i class="el-icon-delete"></i>
          </div>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import _axios from '@/utils/_axios';
export default {
  data() {
    return {
      backend_url: "http://127.0.0.1:5000/get_img/",
      subject_name: "锦城小学射箭社团",
      imglist: [],
      tableData: [],
      tableData2: [],
      tslist:[],
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
    removeimage(url) {
      alert(url);
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
    _axios.post("get_userinfos", data).then(
      success=>{
        this.tx_url = data.back_url + '/get_tx/'+encodeURIComponent(data.subject_name)+'/'+success.tx
        this.subject_info = success.subject_info
        this.teacher_info = success.teacher_info
      },
      err=>{
        console.log(err)
      }
    )
    _axios.get("get_img_list").then(
      (success) => {
         
         let arr = success
         for(let i = 0; i < arr.length; i++)
         {

          arr[i] = "http://127.0.0.1:5000/get_img/"+arr[i];
         }
         this.imglist = arr
      },
      (err) => {

        console.log("err.message", err);
      }
    );
    console.log('token=', this.$store.state.token)
  },
};
</script>

<style scoped>
.img {
  width: 100px;
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
  width: 50%;
  height: 50%;
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
  color:white;
}
</style>