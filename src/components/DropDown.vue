<template>
    <div class="drop-down">
        <b-dropdown id="dropdown" text="Crime Type" class="m-5">
            <b-dropdown-item v-for="murder in murders">{{ murder.murdercount }}</b-dropdown-item>
        </b-dropdown>
        <b-btn id = "legend"  v-b-toggle.collapse1 variant="primary">Legend</b-btn>
        <b-collapse id="collapse1" class="mt-2">
            <b-card>
                <div class="row">
                    <div class="col">Type1</div>
                    <div class="col">Column</div>
                    <div class="w-100"></div>
                    <div class="col">Type2</div>
                    <div class="col">Column</div>
                </div>
            </b-card>
        </b-collapse>
    </div>
</template>

<script>
    export default {
        name: "DropDown.vue",
        data: function() {
            return {
                murders: [{
                    district: 1,
                    murdercount: 100
                },
                    {
                        district: 2,
                        murdercount: 200
                    }
                ]
            }
        },
    }
</script>

<style scoped>
    #legend{
        margin-left:49px;
    }
    b-dropdown {
        width: 100%;
        margin-left: auto;
        margin-right: auto;
    }
    #dropdown {
        width: 200%;
        margin-left: auto;
        margin-right: auto;
    }
</style>