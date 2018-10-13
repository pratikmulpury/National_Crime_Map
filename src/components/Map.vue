<template>
    <div class="Home">
        <div id="wrapper">
            <!--Graphs-->
            <b-container fluid>
                <b-row>
                    <b-col md="12" lg="6" xl="6" class="chartwrapper">
                        <div id="map"></div>
                    </b-col>
                </b-row>
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

                map.addControl(new mapboxgl.Navigation());

            },
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    #map {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 100%;
    }
    
    #wrapper {
        justify-content: center;
    }

    .chartwrapper {
        margin-left: auto;
        margin-right: auto;
        width: 100%;
        height: 100%;
        padding: 0px;
    }
    
    @media only screen and (max-width: 806px) {
        h5 {
            font-size: 13px;
        }
        h6 {
            font-size: 10px;
        }
    }
</style>