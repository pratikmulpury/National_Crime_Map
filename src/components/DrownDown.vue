<template>

    <div class="drop-down">
        <b-dropdown id="ddown1" text="Crime Type" class="m-md-2">
            <b-dropdown-item></b-dropdown-item>
            <b-dropdown-item>Second Action</b-dropdown-item>
            <b-dropdown-item>Third Action</b-dropdown-item>
            <b-dropdown-divider></b-dropdown-divider>
            <b-dropdown-item>Something else here...</b-dropdown-item>
            <b-dropdown-item disabled>Disabled action</b-dropdown-item>
        </b-dropdown>
    </div>
</template>

<script>
    export default {
        name: "DrownDown.vue"
    }
</script>

<style scoped>

</style>