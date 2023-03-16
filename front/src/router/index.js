import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '@/components/LoginView'
import RegistVue from '@/components/RegistVue'

import GaiLan from '@/components/GaiLan'
import JiaoAn from "@/components/JiaoAn"
import ShunJian from "@/components/ShunJian"
import TeSe from '@/components/TeSe'
import ZongJie from '@/components/ZongJie'
import JiHua from '@/components/JiHua'



Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/AboutView.vue')
    },

    {
        path: '/gailan',
        name: 'gailan',
        component: GaiLan

    },
    {
        path: '/login',
        name: 'login',
        component: LoginView

    },
    {
        path: '/regist',
        name: 'regist',
        component: RegistVue

    },
    {
        path: '/jiaoan',
        name: 'jiaoan',
        component: JiaoAn
    },
    {
        path: '/jihua',
        name: 'jihua',
        component: JiHua
    },
    {
        path: '/shunjian',
        name: 'shunjian',
        component: ShunJian
    },
    {
        path: '/zongjie',
        name: 'zongjie',
        component: ZongJie
    },
    {
        path: '/tese',
        name: 'tese',
        component: TeSe
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router