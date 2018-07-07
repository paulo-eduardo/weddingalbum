// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})


if(process.env.NODE_ENV == 'development')
  localStorage.link = "http://localhost:8000"
else
  localStorage.link = "https://weddingalbum.herokuapp.com"