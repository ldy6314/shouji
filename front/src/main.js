import Vue from 'vue'
import ElementUI from 'element-ui'
import "element-ui/lib/theme-chalk/index.css"
import App from './App.vue'
import router from './router'
import store from './store'

Vue.use(ElementUI)
Vue.config.productionTip = false

// router.beforeEach((from, to, next) => {
//     alert(to.path)
//     if (to.path === '/login') {
//         next()
//     } else {
//         let token = localStorage.getItem('token')
//         if (token === null || token === "") {
//             next('/login')
//         } else {
//             next()
//         }
//     }
// })

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')