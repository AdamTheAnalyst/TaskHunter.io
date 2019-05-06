import Vue from 'vue'
import Router from 'vue-router'
import Dashboard from './components/Dashboard'
import Login from './components/Login'
import Register from './components/Register'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: Dashboard,
      meta: {
        title: 'TaskHunter | Simple Life Organisation'
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
      meta: {
        title: 'TaskHunter | Simple Life Organisation'
      }
    },
    {
      path: '/register',
      name: 'register',
      component: Register,
      meta: {
        title: 'TaskHunter | Simple Life Organisation'
      }
    }
  ]
})