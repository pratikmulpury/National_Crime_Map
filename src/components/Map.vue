<template>
    <div class="Home">
        <div id="wrapper">
            <!--Graphs-->
            <b-container fluid>
                <b-row>
                    <b-col id="chloropleth" md="12" lg="6" xl="6" class="chartwrapper">

                    </b-col>
                </b-row>
            </b-container>
        </div>
    </div>
</template>


<script>
    import {
        geojson
    } from './data/py-departments-geojson'
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
            this.createCharts();
        },
        methods: {
            createCharts() {
                // choropleth
                var d3Geo = require("d3-geo")
                var d3Queue = require("d3-queue")
                var width = this.choroplethwidth;
                var height = this.choroplethheight;
                var lowColor = '#f9f9f9'
                var highColor = '#1f7999'
                // D3 Projection

                // credit to brendan sudol for responsivefy method
                function responsivefy(svg) {
                    // get container + svg aspect ratio
                    var container = d3.select(svg.node().parentNode),
                        width = parseInt(svg.style("width")),
                        height = parseInt(svg.style("height")),
                        aspect = width / height;

                    // add viewBox and preserveAspectRatio properties,
                    // and call resize so that svg resizes on inital page load
                    svg.attr("viewBox", "0 0 " + width + " " + height)
                        .attr("preserveAspectRatio", "xMinYMid")
                        .call(resize);

                    d3.select(window).on("resize." + container.attr("id"), resize);

                    // get width of container and resize svg to fit it
                    function resize() {
                        var targetWidth = parseInt(container.style("width"));
                        svg.attr("width", targetWidth);
                        svg.attr("height", Math.round(targetWidth / aspect));
                    }
                }
                // projection of US
                var projection = d3Geo.geoAlbersUsa()
                    .scale([width / 1.05])
                    .translate([width / 2, height / 2]); // scale things down so see entire US
                // Define path generator
                var path = d3Geo.geoPath() // path generator that will convert GeoJSON to SVG paths
                    .projection(projection); // tell path generator to use albersUsa projection
                //Create or select SVG element and append map to the SVG
                var keys = Object.keys(d3.select("svg"));
                var svg = [];
                if (d3.select("svg")[keys[0]][0][0] == null) {
                    svg = d3.select("#chloropleth")
                        .append("svg")
                        .attr("width", width)
                        .attr("height", height)
                        .call(responsivefy);
                } else {
                    svg = d3.select("svg");
                }


                // color by ratio of patients in IRIS to state population
                var minVal = d3.min(ratio)
                var maxVal = d3.max(ratio)

                var ramp = d3.scaleLinear().domain([minVal, maxVal]).range([lowColor, highColor])
                // Load GeoJSON data and merge with states data
                var json = this.usjson;
                for (var i = 0; i < patients.length; i++) {
                    // Grab State Name
                    var dataState = states[i];
                    // Grab data value 
                    var dataValue = ratio[i];
                    // Find the corresponding state inside the GeoJSON
                    for (var j = 0; j < json.features.length; j++) {
                        var jsonState = json.features[j].properties.name;
                        if (dataState == jsonState) {
                            // Copy the data value into the JSON
                            json.features[j].properties.value = dataValue;
                            json.features[j].properties.value2 = patients[i];
                            // Stop looking through the JSON
                            break;
                        }
                    }
                }

                // color based on ratio of patients to state population
                var paths = svg.selectAll("path")
                    .data(json.features)
                    .enter()
                    .append("path")
                    .attr("d", path)
                    .style("stroke", "#fff")
                    .style("stroke-width", "1")
                    .style("fill", function(d) {
                        return ramp(d.properties.value)
                    });

                // add and position text labels indicating number of patients in IRIS per state
                var labels = svg.append("svg:g")
                    .attr("id", "labels")
                    .attr("class", "Title");
            }
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