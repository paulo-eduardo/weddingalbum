import Vue from 'vue'
import Router from 'vue-router'
import ApprovingPictures from '../views/ApprovingPictures.vue'
import PublicPictures from '../views/PublicPictures.vue'
import UploadView from '../views/UploadView.vue'
import LoginView from '../views/LoginView.vue'



Vue.use(Router)

const router = new Router({
  routes: [
    {
      path: '/',
      name: 'PublicPictures',
      component: PublicPictures
    },
    {
      path: '/Approving',
      name: 'ApprovingPictures',
      component: ApprovingPictures
    },
    {
      path: '/Upload',
      name: 'UploadView',
      component: UploadView
    },
    {
      path: '/Login',
      name: 'LoginView',
      component: LoginView
    }
  ]
})

router.beforeEach((to, from, next) => {
  if(to.path === '/Aprovacao') {
      if(localStorage.token) { 
          next();
      } else {
          next('Login');
      }
  } else {
      next();
  }
})

export default router
