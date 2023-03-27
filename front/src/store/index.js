import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        token: "",
        subject_name: " ",
        role: 0,
    },
    getters: {
        token: (state) => {
            return state.token
        }
    },
    mutations: {
        LOGIN: (state, value) => {
            console.log("login 被调用", state, value)
            state.token = value.token
            state.role = value.role
        },
    },
    actions: {},
    modules: {}
})