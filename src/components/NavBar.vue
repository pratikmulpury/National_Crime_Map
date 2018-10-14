<template>
    <div id="nav">
        <b-navbar toggleable="md" type="dark">
            <b-navbar-brand href="#">
                <img class="logo" src="https://learnstuff.io/img/favicon.png"/>
            </b-navbar-brand>
            <b-navbar-toggle target="nav_collapse">
            </b-navbar-toggle>
            <b-collapse  is-nav id="nav_collapse">
                <b-navbar-nav>
                    <b-nav-item class="links" :to="{name:'home'}">Home</b-nav-item>
                    <b-nav-item class="links" :to="{name:'map'}">Map</b-nav-item>
                </b-navbar-nav>
            </b-collapse>
            <SearchBar></SearchBar>
        </b-navbar>
    </div>
</template>

<script>
    import SearchBar from "./SearchBar"
    export default {
        name: "NavBar.vue",
        components: { SearchBar },
    }
</script>

<style scoped>
    img {
        width: 50px;
        height: 50px;
        margin: 10px;
    }

    @media only screen and (max-width: 640px) {
        img {
            width: 50px !important;
            height: 50px !important;
        }
    }

    @media only screen and (max-width: 640px) {
        SearchBar {
            position: static;
            width: auto;
        }
    }

</style>