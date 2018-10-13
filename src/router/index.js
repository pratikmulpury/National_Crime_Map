import Vue from 'vue'
import Router from 'vue-router'
import VueRouter from 'vue-router'
import Home from '@/components/Home'
import Map from '@/components/Map'

Vue.use(Router)

Vue.use(VueRouter);


export default new Router({

  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
       beforeEnter: (to, from, next) => {
        const { uri } = to.query;
        if (uri != null && uri != '/') {
            next(false);
            router.push(uri);
        } else {
            next();
        }
      }
    },  
    {
      name:'map',
      path:'/map',
      component:Map,
       beforeEnter: (to, from, next) => {
        const { uri } = to.query;
        if (uri != null && uri != '/') {
            next(false);
            router.push(uri);
        } else {
            next();
        }
      } 
    },
    {
      name:'Noexistingpath',
      path :'*',
      component:Map,
      beforeEnter: (to, from, next) => {
        const { uri } = to.query;
        if (uri != null && uri != '/') {
            next(false);
            router.push(uri);
        } else {
            next();
        }
      }
    }
  ]
})
