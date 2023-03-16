import axios from 'axios'
import { Message } from 'element-ui';
const _axios = axios.create({
    timeout: 5000,

});
_axios.interceptors.request.use(config => {
    let token = localStorage.getItem('token')
    if(token){
        config.headers.common['token'] = token
    }
    return config
},
error=>{
    return Promise.reject(error)
}
)

_axios.interceptors.response.use((res) => {

    return res.data
},
    (error) => {
        if( error.response.status === 401)
            Message({
                'message': error.response.data['message'],
                'type': 'error'
            })
            return Promise.reject(error.response.data)
    }

)
export default _axios