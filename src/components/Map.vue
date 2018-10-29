<template>
    <div class="Home">
        <div id="wrapper">
            <!--Graphs-->
            <b-container fluid>
                <div id="map"></div>
            </b-container>
        </div>
    </div>
</template>


<script>
    import * as d3 from "d3";
    import * as mapboxgl from 'mapbox-gl'
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
            this.drawMap();
        },
        updated() {
            // create charts
            this.drawMap();
        },
        methods: {
            drawMap() {
                mapboxgl.accessToken = 'pk.eyJ1Ijoic2hpbWl6dSIsImEiOiI0cl85c2pNIn0.RefZMaOzNn-IistVe-Zcnw'

                //Setup mapbox-gl map
                var map = new mapboxgl.Map({
                    container: 'map', // container id
                    style: 'mapbox://styles/mapbox/streets-v8',
                    center: [-78.89, 35.99],
                    zoom: 12,
                })
                map.fitBounds([[
                    -78.89,
                    -35.99
                ]]);
            },
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    #map{
        min-height:500px;
        max-width:800px;
    }
    .Home {
        padding-top: 20px;
    }
    #wrapper {
        justify-content: center;
    }
    
    @media only screen and (max-width: 806px) {
        h5 {
            font-size: 13px;
        }
        h6 {
            font-size: 10px;
        }
    }
    @media only screen and (min-width: 1100px) {
        #map{
            min-height:500px;
            max-width:800px;
        }
    }
</style>