import Vue from 'vue'
import VeeValidate from 'vee-validate'
import axios from 'axios'
import VueAxios from 'vue-axios'
import Datetime from 'vue-datetime'
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'vue-datetime/dist/vue-datetime.css'

import App from './App.vue'
import router from './router'

Vue.use(VeeValidate);
Vue.use(VueAxios, axios);
Vue.use(BootstrapVue);
Vue.use(Datetime);
Vue.config.productionTip = false

import config from "./settings.json";
Vue.prototype.api_config = config;

router.beforeEach((to, from, next) => {
  document.title = to.meta.title
  next()
})

import moment from 'moment'
import store from './store'

Vue.filter('formatDateDue', function(value) {
  if (value) {
    return moment(String(value)).fromNow()
  }
})

Vue.filter('formatDateCalendar', function(value) {
  if (value) {
    return moment(String(value)).calendar()
  }
})

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
