import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '@/components/LoginView'
import RegistVue from '@/components/RegistVue'
import WordsVue from '@/components/WordsVue'
import PastVue from '@/components/PastVue'
import TotVue from '@/components/TotVue'
import CompareVue from '@/components/CompareVue'
import AddVue from '@/components/AddVue'
import TestVue from '@/components/TestVue'
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
        path: '/myword',
        name: 'word',
        component: WordsVue,
        children: [{
                path: 'tot',
                name: 'tot',
                component: TotVue
            },
            {
                path: 'past',
                name: 'past',
                component: PastVue
            },
            {
                path: 'compare',
                name: 'compare',
                component: CompareVue
            },
            {
                path: 'add',
                name: 'add',
                component: AddVue
            },
            {
                path: 'test',
                name: 'test',
                component: TestVue
            },

        ]
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router