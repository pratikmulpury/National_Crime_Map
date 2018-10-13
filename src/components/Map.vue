<template>
    <div class="Home">
        <div id="wrapper">
            <!--Graphs-->
            <b-container fluid>
                <b-row>
                    <b-col id="chloropleth" md="12" lg="6" xl="6" class="chartwrapper">
                        <div id="map"></div>
                    </b-col>
                </b-row>
            </b-container>
        </div>
    </div>
</template>


<script>
    import * as d3 from "d3";
    import usjson from './data/us-states.json'
    
    
    export default {
        name: 'Demographics',
        data() {
            return {
                queryresults: '',
                usjson: usjson,
                choroplethheight: 227,
                choroplethwidth: 520,
            }
        },
        mounted() {
            // create charts
            let map  = document.createElement('script');
            map.setAttribute('src', 'https://api.tiles.mapbox.com/mapbox-gl-js/v0.12.0/mapbox-gl.js');
            document.head.appendChild(map);
            this.drawMap();
        },
        methods: {
            drawMap() {
                mapboxgl.accessToken = 'pk.eyJ1Ijoic2hpbWl6dSIsImEiOiI0cl85c2pNIn0.RefZMaOzNn-IistVe-Zcnw'

                //Setup mapbox-gl map
                var map = new mapboxgl.Map({
                    container: 'map', // container id
                    style: 'mapbox://styles/mapbox/streets-v8',
                    center: [141.15448379999998, 39.702053　],
                    zoom: 4,
                })

                map.addControl(new mapboxgl.Navigation());
            },
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    #statetitle {
        text-align: center;
        font-weight: bold;
        color: #666 !important;
        font-size: 12px;
        margin-top: 10px;
    }
    
    #firstbutton {
        margin-top: 0px;
    }
    
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