<template>
    <div class="search-bar">
        <b-nav-form>
            <b-form-input size="sm" class="mr-sm-2" type="text" placeholder="Enter the city"/>
            <b-button size="sm" class="my-2 my-sm-0" type="submit" @click="search">Search</b-button>
        </b-nav-form>
    </div>
</template>

<script>
    export default {
        name: "SearchBar.vue",
        methods: {
            search() {
                console.log(this.query);
                this.$router.push({ name: "search", params: { query: this.query } });
            }
        }
    }
</script>

<style scoped>

</style>