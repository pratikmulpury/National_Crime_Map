<template>
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
        </b-navbar>
    </div>
</template>

<script>
    export default {
        name: "NavBar.vue"
    }
</script>

<style scoped>

</style>