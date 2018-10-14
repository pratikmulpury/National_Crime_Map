<template>
  <div id="app">
    <NavBar></NavBar>
    <div class="row">
      <div class="col-xl">
        <Map></Map>
      </div>
      <div class="col-sm">
        <DropDown></DropDown>
      </div>
    </div>
    <Footer></Footer>
  </div>
</template>

<script>
  import BootstrapVue from 'bootstrap-vue'
  import NavBar from "./components/NavBar"
  import Map from "./components/Map"
  import DropDown from "./components/DrownDown"
  import Footer from "./components/Footer"
  import Vue from 'vue'
  Vue.use(BootstrapVue);
  import 'bootstrap/dist/css/bootstrap.css'
  import 'bootstrap-vue/dist/bootstrap-vue.css'

  export default {
    components: { NavBar, Map, DropDown, Footer },
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
  
  .links a {
    color: #1A1A1A !important;
    margin-top: -4px;
  }
  
  .links a:hover {
    color: #1F7999 !important;
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


