import axios from 'axios'
import { Message } from 'element-ui'

/****** 创建axios实例 ******/
const _axios = axios.create({
    // baseURL: "http:127.0.0.1:5000",
    timeout: 5000 // 请求超时时间
})

_axios.interceptors.request.use(
    config => {
        config.headers['token'] = localStorage.getItem('token')
        return config
    },
    error => {
        console.log(error)
        return Promise.reject(error)
    }
)

/****** respone拦截器==>对响应做处理 ******/
_axios.interceptors.response.use(
    response => {
        //这里根据后端提供的数据进行对应的处理

        return response.data;

    },
    error => {
        if(error.response.status==401)
        {
            Message({
              message:"账号或者密码错误",
              type: 'error'  
            })
        }
        return Promise.reject(error)
    }
)

export default _axios;