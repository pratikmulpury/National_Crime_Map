<template>
  <div id="app">
    <!--Navbar-->
    <div id="nav">
      <b-navbar toggleable="md" type="light">
        <b-navbar-brand href="#">
          <img src="/static/Logo-wide-white.png" />
        </b-navbar-brand>
        <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
        <b-collapse  is-nav id="nav_collapse">
          <b-navbar-nav right>
            <b-nav-item class="links" :to="{name:'home'}">Home</b-nav-item>
            <b-nav-item class="links" :to="{name:'map'}">Map</b-nav-item>
          </b-navbar-nav>
        </b-collapse>
        <span > Test </span>
      </b-navbar>
    </div>
    <!--Component to be Displayed-->
    <router-view></router-view>
  </div>
</template>

<script>
  import BootstrapVue from 'bootstrap-vue'
  
  import Vue from 'vue'
  Vue.use(BootstrapVue);
  import 'bootstrap/dist/css/bootstrap.css'
  import 'bootstrap-vue/dist/bootstrap-vue.css'
  import axios from 'axios'
  import Router from './router';

  export default {
  
    data() {
      return {
        name: 'App'
      }
    },
  }
</script>i

<style>
  @import url('https://fonts.googleapis.com/css?family=Lato');
  #app {
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }
  
  #link {
    background: none !important;
    border: none !important;
    cursor: pointer !important;
    font-size: 12px !important;
    position: absolute !important;
    top: 0 !important;
    right: 0 !important;
    margin-right: 10px !important;
    z-index: 10 !important;
  }
  
  #signout {
    padding-bottom: 3px !important;
  }
  
  #nav {
    background: #f5fafb !important;
    background-color: #f5fafb !important;
    position: relative !important;
  }
  #link:hover {
    color: #1F7999 !important;
  }
  
  .links a {
    color: #1A1A1A !important;
    margin-top: -4px;
  }
  
  .links a:hover {
    color: #1F7999 !important;
  }
  
  img {
    width: 250px !important;
    height: auto !important;
    margin-top: -16px !important;
  }
  
  span {
    font-size: 24px !important;
    color: #1A1A1A !important;
  }
  
  @media only screen and (min-width: 640px) {
    span {
      margin-top: -9px !important;
    }
  }
  
  @media only screen and (max-width: 640px) {
    img {
      width: 150px !important;
      height: auto !important;
    }
    span {
      font-size: 14px !important;
    }
  }
  
  body {
    margin: 0 !important;
    font-family: 'Lato', sans-serif !important;
  }
  
  .navbar {
    background: #f5fafb !important;
  }
</style>


