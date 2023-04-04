import Vue from 'vue'
import Vuex from 'vuex'
import { back_url } from '@/utils/config'
Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        token: "",
        subject_name: " ",
        role: 0,
        logined: false,
        back_url: back_url
    },
    getters: {
        token: (state) => {
            return state.token
        },
        back_url: (state) => {
            return state.back_url
        }
    },
    mutations: {
        LOGIN: (state, value) => {
            console.log("login 被调用", state, value)
            state.token = value.token
            state.role = value.role
            if(value.token=="")
                state.logined = false
            else
                state.logined = true
        },
    },
    actions: {},
    modules: {}
})