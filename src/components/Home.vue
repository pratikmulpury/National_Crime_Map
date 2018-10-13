<template>
  <div class="Home">
    
  </div>
</template>

<script>
  
  export default {
    name: 'Home',
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  #wrapper {
    justify-content: center;
  }
  
  .card-header {
    border: none;
    background-color: #1f7999 !important;
  }
  
  .card-body {
    padding-bottom: .3em !important;
    padding-top: .3em !important;
  }
  
  .card-text {
    line-height: 1;
    color: #1f7999;
  }
  
  h5 {
    font-size: 17px;
  }
  
  h6 {
    font-size: 14px;
  }
  
  .btn-primary {
    display: none !important;
  }
  
  @media only screen and (max-width: 806px) {
    h5 {
      font-size: 13px;
    }
    h6 {
      font-size: 10px;
    }
  }
  
  .box-shadow:after {
    content: "";
    position: absolute;
    width: 100%;
    bottom: 1px;
    z-index: -1;
    transform: scale(.96);
    box-shadow: 0px 0px 8px 4px #5E6D7C;
  }
  
  #importantstats {
    /* background-color: #1A1A1A !important;*/
    border: 1px solid !important;
    background-color: #F0F0F0 !important;
    margin-top: 10px;
    margin-left: 10px;
    margin-right: 10px;
  }
</style>