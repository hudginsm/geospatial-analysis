from workers import WorkerEntrypoint, Response

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        html = """
        <!DOCTYPE html>
        <html>
        <head>
            
            <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
            <script src="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.js"></script>
            <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.9.3/dist/leaflet.css"/>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css"/>
            <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.0.0/css/bootstrap-glyphicons.css"/>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6.2.0/css/all.min.css"/>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/python-visualization/folium/folium/templates/leaflet.awesome.rotate.min.css"/>
            
                    <meta name="viewport" content="width=device-width,
                        initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
                    <style>
                        #map_67587efcd21f46d2e6582df8c3c5f5ac {
                            position: relative;
                            width: 100.0%;
                            height: 100.0%;
                            left: 0.0%;
                            top: 0.0%;
                        }
                        .leaflet-container { font-size: 1rem; }
                    </style>
        
                    <style>html, body {
                        width: 100%;
                        height: 100%;
                        margin: 0;
                        padding: 0;
                    }
                    </style>
        
                    <style>#map {
                        position:absolute;
                        top:0;
                        bottom:0;
                        right:0;
                        left:0;
                        }
                    </style>
        
                    <script>
                        L_NO_TOUCH = false;
                        L_DISABLE_3D = false;
                    </script>
        
                
            
                            <style>
                                .foliumtooltip {
                                    
                                }
                               .foliumtooltip table{
                                    margin: auto;
                                }
                                .foliumtooltip tr{
                                    text-align: left;
                                }
                                .foliumtooltip th{
                                    padding: 2px; padding-right: 8px;
                                }
                            </style>
                    
            
                            <style>
                                .foliumpopup {
                                    margin: auto;
                                }
                               .foliumpopup table{
                                    margin: auto;
                                }
                                .foliumpopup tr{
                                    text-align: left;
                                }
                                .foliumpopup th{
                                    padding: 2px; padding-right: 8px;
                                }
                            </style>
                    
            
            <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
            <script>$( function() {
                $( ".maplegend" ).draggable({
                    start: function (event, ui) {
                        $(this).css({
                            right: "auto",
                            top: "auto",
                            bottom: "auto"
                        });
                    }
                });
            });
            </script>
            <style type='text/css'>
              .maplegend {
                position: absolute;
                z-index:9999;
                background-color: rgba(255, 255, 255, .8);
                border-radius: 5px;
                box-shadow: 0 0 15px rgba(0,0,0,0.2);
                padding: 10px;
                font: 12px/14px Arial, Helvetica, sans-serif;
                right: 10px;
                bottom: 20px;
              }
              .maplegend .legend-title {
                text-align: left;
                margin-bottom: 5px;
                font-weight: bold;
                }
              .maplegend .legend-scale ul {
                margin: 0;
                margin-bottom: 0px;
                padding: 0;
                float: left;
                list-style: none;
                }
              .maplegend .legend-scale ul li {
                list-style: none;
                margin-left: 0;
                line-height: 16px;
                margin-bottom: 2px;
                }
              .maplegend ul.legend-labels li span {
                display: block;
                float: left;
                height: 14px;
                width: 14px;
                margin-right: 5px;
                margin-left: 0;
                border: 0px solid #ccc;
                }
              .maplegend .legend-source {
                color: #777;
                clear: both;
                }
              .maplegend a {
                color: #777;
                }
            </style>
            
        </head>
        <body>
            
            
            <div id='maplegend Company' class='maplegend'>
                <div class='legend-title'>Company</div>
                <div class='legend-scale'>
                    <ul class='legend-labels'>
                        <li><span style='background:firebrick'></span>Firehouse</li>
                        <li><span style='background:blue'></span>Jersey Mikes</li>
                        <li><span style='background:fuchsia'></span>Jimmy Johns</li>
                        <li><span style='background:darkgreen'></span>Subway</li>
                    </ul>
                </div>
            </div>
            
            
                    <div class="folium-map" id="map_67587efcd21f46d2e6582df8c3c5f5ac" ></div>
                
        </body>
        <script>
            
            
                    var map_67587efcd21f46d2e6582df8c3c5f5ac = L.map(
                        "map_67587efcd21f46d2e6582df8c3c5f5ac",
                        {
                            center: [33.5693345, -86.82503700000001],
                            crs: L.CRS.EPSG3857,
                            ...{
          "zoom": 10.5,
          "zoomControl": true,
          "preferCanvas": false,
        }
        
                        }
                    );
                    L.control.scale().addTo(map_67587efcd21f46d2e6582df8c3c5f5ac);
        
                    
        
                
            
                    var tile_layer_5fa1e1cdbef448731fd74d6efcc15cde = L.tileLayer(
                        "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                        {
          "minZoom": 0,
          "maxZoom": 19,
          "maxNativeZoom": 19,
          "noWrap": false,
          "attribution": "\u0026copy; \u003ca href=\"https://www.openstreetmap.org/copyright\"\u003eOpenStreetMap\u003c/a\u003e contributors",
          "subdomains": "abc",
          "detectRetina": false,
          "tms": false,
          "opacity": 1,
        }
        
                    );
                
            
                    tile_layer_5fa1e1cdbef448731fd74d6efcc15cde.addTo(map_67587efcd21f46d2e6582df8c3c5f5ac);
                
            
                function geo_json_710392236cf02b4b9c99530d1a816795_styler(feature) {
                    switch(feature.properties.Name) {
                        case "JIMMY JOHNS #4178  1919 11TH AVE S BIRMINGHAM 35205  ": case "JIMMY JOHNS #4168  323 20TH ST N BIRMINGHAM 35203  ": case "JIMMY JOHNS #3561  5431 PATRICK WAY BIRMINGHAM 35235  ": case "JIMMY JOHNS #3014  1919 KENTUCKY AVE VESTAVIA HILLS 35216  ": case "JIMMY JOHNS #3013  5250 MEDFORD DR HOOVER 35244  ": case "JIMMY JOHNS #2034  3411 COLONNADE PKWY BIRMINGHAM 35243  ": case "JIMMY JOHNS #1657  4730 CHASE CIR HOOVER 35244  ": 
                            return {"color": "fuchsia", "fillColor": "fuchsia", "fillOpacity": 0.5, "weight": 2};
                        case "JERSEY MIKES SUBS #12011  1031 MONTGOMERY HWY VESTAVIA HILLS 35216  ": case "JERSEY MIKES SUBS #12009  3150 OVERTON RD MOUNTAIN BROOK 35223  ": case "JERSEY MIKES SUBS #12007  1851 MONTGOMERY HIGHWAY HOOVER 35244  ": case "JERSEY MIKES SUBS  1808 GADSDEN HWY TRUSSVILLE 35235  ": case "JERSEY MIKES SUBS  626 KERR DR GARDENDALE 35071  ": 
                            return {"color": "blue", "fillColor": "blue", "fillOpacity": 0.5, "weight": 2};
                        case "FIREHOUSE SUBS  1483 GADSDEN HWY BIRMINGHAM 35235  ": case "FIREHOUSE SUBS  3477 LOWERY PKWY FULTONDALE 35068  ": case "FIREHOUSE SUBS  808 GREEN SPRINGS HWY HOMEWOOD 35209  ": case "FIREHOUSE SUBS  4867 PROMENADE PKWY BESSEMER 35022  ": case "FIREHOUSE SUBS  1580 MONTGOMERY HWY HOOVER 35216  ": 
                            return {"color": "firebrick", "fillColor": "firebrick", "fillOpacity": 0.5, "weight": 2};
                        default:
                            return {"color": "darkgreen", "fillColor": "darkgreen", "fillOpacity": 0.5, "weight": 2};
                    }
                }
                function geo_json_710392236cf02b4b9c99530d1a816795_highlighter(feature) {
                    switch(feature.properties.Name) {
                        default:
                            return {"fillOpacity": 0.75};
                    }
                }
                function geo_json_710392236cf02b4b9c99530d1a816795_pointToLayer(feature, latlng) {
                    var opts = {
          "stroke": true,
          "color": "#3388ff",
          "weight": 3,
          "opacity": 1.0,
          "lineCap": "round",
          "lineJoin": "round",
          "dashArray": null,
          "dashOffset": null,
          "fill": true,
          "fillColor": "#3388ff",
          "fillOpacity": 0.2,
          "fillRule": "evenodd",
          "bubblingMouseEvents": true,
          "radius": 5,
        };
                    
                    let style = geo_json_710392236cf02b4b9c99530d1a816795_styler(feature)
                    Object.assign(opts, style)
                    
                    return new L.CircleMarker(latlng, opts)
                }
        
                function geo_json_710392236cf02b4b9c99530d1a816795_onEachFeature(feature, layer) {
        
                    layer.on({
                        mouseout: function(e) {
                            if(typeof e.target.setStyle === "function"){
                                    geo_json_710392236cf02b4b9c99530d1a816795.resetStyle(e.target);
                            }
                        },
                        mouseover: function(e) {
                            if(typeof e.target.setStyle === "function"){
                                const highlightStyle = geo_json_710392236cf02b4b9c99530d1a816795_highlighter(e.target.feature)
                                e.target.setStyle(highlightStyle);
                            }
                        },
                    });
                };
                var geo_json_710392236cf02b4b9c99530d1a816795 = L.geoJson(null, {
                        onEachFeature: geo_json_710392236cf02b4b9c99530d1a816795_onEachFeature,
                    
                        style: geo_json_710392236cf02b4b9c99530d1a816795_styler,
                        pointToLayer: geo_json_710392236cf02b4b9c99530d1a816795_pointToLayer,
                    ...{
        }
                });
        
                function geo_json_710392236cf02b4b9c99530d1a816795_add (data) {
                    geo_json_710392236cf02b4b9c99530d1a816795
                        .addData(data);
                }
                    geo_json_710392236cf02b4b9c99530d1a816795_add({"bbox": [-87.070588, 33.328199, -86.579486, 33.81047], "features": [{"bbox": [-86.796872, 33.500092, -86.796872, 33.500092], "geometry": {"coordinates": [-86.796872, 33.500092], "type": "Point"}, "id": "0", "properties": {"Company": "Jimmy Johns", "Date": "08/18/25", "Name": "JIMMY JOHNS #4178  1919 11TH AVE S BIRMINGHAM 35205  ", "Permit": 28573, "Score": 92, "Smoke Free": "Y", "__folium_color": "fuchsia", "address": "Jimmy John\u0027s"}, "type": "Feature"}, {"bbox": [-86.807232, 33.517176, -86.807232, 33.517176], "geometry": {"coordinates": [-86.807232, 33.517176], "type": "Point"}, "id": "1", "properties": {"Company": "Jimmy Johns", "Date": "06/03/25", "Name": "JIMMY JOHNS #4168  323 20TH ST N BIRMINGHAM 35203  ", "Permit": 28574, "Score": 95, "Smoke Free": "Y", "__folium_color": "fuchsia", "address": "Jimmy John\u0027s"}, "type": "Feature"}, {"bbox": [-86.625928, 33.609204, -86.625928, 33.609204], "geometry": {"coordinates": [-86.625928, 33.609204], "type": "Point"}, "id": "2", "properties": {"Company": "Jimmy Johns", "Date": "02/13/25", "Name": "JIMMY JOHNS #3561  5431 PATRICK WAY BIRMINGHAM 35235  ", "Permit": 28575, "Score": 98, "Smoke Free": "Y", "__folium_color": "fuchsia", "address": "Jimmy John\u0027s"}, "type": "Feature"}, {"bbox": [-86.792274, 33.446996, -86.792274, 33.446996], "geometry": {"coordinates": [-86.792274, 33.446996], "type": "Point"}, "id": "3", "properties": {"Company": "Jimmy Johns", "Date": "03/10/25", "Name": "JIMMY JOHNS #3014  1919 KENTUCKY AVE VESTAVIA HILLS 35216  ", "Permit": 28576, "Score": 95, "Smoke Free": "Y", "__folium_color": "fuchsia", "address": "Jimmy John\u0027s"}, "type": "Feature"}, {"bbox": [-86.854875, 33.356178, -86.854875, 33.356178], "geometry": {"coordinates": [-86.854875, 33.356178], "type": "Point"}, "id": "4", "properties": {"Company": "Jimmy Johns", "Date": "08/05/25", "Name": "JIMMY JOHNS #3013  5250 MEDFORD DR HOOVER 35244  ", "Permit": 28577, "Score": 95, "Smoke Free": "Y", "__folium_color": "fuchsia", "address": "Jimmy John\u0027s"}, "type": "Feature"}, {"bbox": [-86.729371, 33.438582, -86.729371, 33.438582], "geometry": {"coordinates": [-86.729371, 33.438582], "type": "Point"}, "id": "5", "properties": {"Company": "Jimmy Johns", "Date": "04/08/25", "Name": "JIMMY JOHNS #2034  3411 COLONNADE PKWY BIRMINGHAM 35243  ", "Permit": 28578, "Score": 91, "Smoke Free": "Y", "__folium_color": "fuchsia", "address": "Jimmy John\u0027s"}, "type": "Feature"}, {"bbox": [-86.799744, 33.368684, -86.799744, 33.368684], "geometry": {"coordinates": [-86.799744, 33.368684], "type": "Point"}, "id": "6", "properties": {"Company": "Jimmy Johns", "Date": "08/05/25", "Name": "JIMMY JOHNS #1657  4730 CHASE CIR HOOVER 35244  ", "Permit": 28572, "Score": 94, "Smoke Free": "Y", "__folium_color": "fuchsia", "address": "Jimmy John\u0027s"}, "type": "Feature"}, {"bbox": [-86.788297, 33.439213, -86.788297, 33.439213], "geometry": {"coordinates": [-86.788297, 33.439213], "type": "Point"}, "id": "0", "properties": {"Company": "Jersey Mikes", "Date": "02/21/25", "Name": "JERSEY MIKES SUBS #12011  1031 MONTGOMERY HWY VESTAVIA HILLS 35216  ", "Permit": 25085, "Score": 95, "Smoke Free": "Y", "__folium_color": "blue", "address": "Jersey Mike\u0027s"}, "type": "Feature"}, {"bbox": [-86.733081, 33.467415, -86.733081, 33.467415], "geometry": {"coordinates": [-86.733081, 33.467415], "type": "Point"}, "id": "1", "properties": {"Company": "Jersey Mikes", "Date": "08/07/25", "Name": "JERSEY MIKES SUBS #12009  3150 OVERTON RD MOUNTAIN BROOK 35223  ", "Permit": 25086, "Score": 94, "Smoke Free": "Y", "__folium_color": "blue", "address": "Jersey Mike\u0027s"}, "type": "Feature"}, {"bbox": [-86.798267, 33.370209, -86.798267, 33.370209], "geometry": {"coordinates": [-86.798267, 33.370209], "type": "Point"}, "id": "2", "properties": {"Company": "Jersey Mikes", "Date": "08/12/25", "Name": "JERSEY MIKES SUBS #12007  1851 MONTGOMERY HIGHWAY HOOVER 35244  ", "Permit": 25084, "Score": 91, "Smoke Free": "Y", "__folium_color": "blue", "address": "Jersey Mike\u0027s"}, "type": "Feature"}, {"bbox": [-86.632008, 33.60685, -86.632008, 33.60685], "geometry": {"coordinates": [-86.632008, 33.60685], "type": "Point"}, "id": "3", "properties": {"Company": "Jersey Mikes", "Date": "02/10/25", "Name": "JERSEY MIKES SUBS  1808 GADSDEN HWY TRUSSVILLE 35235  ", "Permit": 27254, "Score": 97, "Smoke Free": "Y", "__folium_color": "blue", "address": "Jersey Mike\u0027s"}, "type": "Feature"}, {"bbox": [-86.824265321169, 33.653328718456, -86.824265321169, 33.653328718456], "geometry": {"coordinates": [-86.824265321169, 33.653328718456], "type": "Point"}, "id": "4", "properties": {"Company": "Jersey Mikes", "Date": "08/08/25", "Name": "JERSEY MIKES SUBS  626 KERR DR GARDENDALE 35071  ", "Permit": 28142, "Score": 90, "Smoke Free": "Y", "__folium_color": "blue", "address": "626 Kerr Dr, Gardendale, Alabama, 35071"}, "type": "Feature"}, {"bbox": [-87.001276, 33.3613, -87.001276, 33.3613], "geometry": {"coordinates": [-87.001276, 33.3613], "type": "Point"}, "id": "0", "properties": {"Company": "Subway", "Date": "06/09/25", "Name": "SUBWAY RESTAURANT  750 ACADEMY DR BESSEMER 35022  ", "Permit": 28216, "Score": 94, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.647688, 33.597149, -86.647688, 33.597149], "geometry": {"coordinates": [-86.647688, 33.597149], "type": "Point"}, "id": "1", "properties": {"Company": "Subway", "Date": "04/16/25", "Name": "SUBWAY #6252  1930 EDWARDS LAKE RD TRUSSVILLE 35235  ", "Permit": 18279, "Score": 90, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-87.070588, 33.481536, -87.070588, 33.481536], "geometry": {"coordinates": [-87.070588, 33.481536], "type": "Point"}, "id": "2", "properties": {"Company": "Subway", "Date": "08/11/25", "Name": "SUBWAY #60054  6817 WARRIOR RIVER RD BESSEMER 35023  ", "Permit": 20561, "Score": 100, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.812698546244, 33.746234194257, -86.812698546244, 33.746234194257], "geometry": {"coordinates": [-86.812698546244, 33.746234194257], "type": "Point"}, "id": "3", "properties": {"Company": "Subway", "Date": "05/01/25", "Name": "SUBWAY #57189  8311 US HWY 31 N MORRIS 35116  ", "Permit": 26836, "Score": 95, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "8311 Highway 31 N, Morris, Alabama, 35116"}, "type": "Feature"}, {"bbox": [-86.800968, 33.506077, -86.800968, 33.506077], "geometry": {"coordinates": [-86.800968, 33.506077], "type": "Point"}, "id": "4", "properties": {"Company": "Subway", "Date": "08/05/25", "Name": "SUBWAY #46968 - UAB Hospital  625 19TH ST S BIRMINGHAM 35233  ", "Permit": 21395, "Score": 93, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.820821, 33.447021, -86.820821, 33.447021], "geometry": {"coordinates": [-86.820821, 33.447021], "type": "Point"}, "id": "5", "properties": {"Company": "Subway", "Date": "05/09/25", "Name": "SUBWAY #37573  209 LAKESHORE PKWY HOMEWOOD 35209  ", "Permit": 15914, "Score": 92, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.579486, 33.638288, -86.579486, 33.638288], "geometry": {"coordinates": [-86.579486, 33.638288], "type": "Point"}, "id": "6", "properties": {"Company": "Subway", "Date": "03/21/25", "Name": "SUBWAY #36657  4643 CAMP COLEMAN RD TRUSSVILLE 35173  ", "Permit": 24686, "Score": 100, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.683088, 33.640454, -86.683088, 33.640454], "geometry": {"coordinates": [-86.683088, 33.640454], "type": "Point"}, "id": "7", "properties": {"Company": "Subway", "Date": "02/07/25", "Name": "SUBWAY #3648  2103 CENTER POINT RD BIRMINGHAM 35215  ", "Permit": 19084, "Score": 98, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.783636, 33.551395, -86.783636, 33.551395], "geometry": {"coordinates": [-86.783636, 33.551395], "type": "Point"}, "id": "8", "properties": {"Company": "Subway", "Date": "06/13/25", "Name": "SUBWAY #34790  1700 TALLAPOOSA ST BIRMINGHAM 35234  ", "Permit": 28238, "Score": 89, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.866222, 33.438208, -86.866222, 33.438208], "geometry": {"coordinates": [-86.866222, 33.438208], "type": "Point"}, "id": "9", "properties": {"Company": "Subway", "Date": "05/05/25", "Name": "SUBWAY #34716  100 FRANKFURT CIR BIRMINGHAM 35211  ", "Permit": 22779, "Score": 96, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.702189, 33.479365, -86.702189, 33.479365], "geometry": {"coordinates": [-86.702189, 33.479365], "type": "Point"}, "id": "10", "properties": {"Company": "Subway", "Date": "07/03/25", "Name": "SUBWAY #33765  8000 LIBERTY PKWY VESTAVIA HILLS 35242  ", "Permit": 19252, "Score": 99, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.822145, 33.81047, -86.822145, 33.81047], "geometry": {"coordinates": [-86.822145, 33.81047], "type": "Point"}, "id": "11", "properties": {"Company": "Subway", "Date": "04/17/25", "Name": "SUBWAY #29169  290 CANE CREEK RD WARRIOR 35180  ", "Permit": 22403, "Score": 93, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.806618, 33.415858, -86.806618, 33.415858], "geometry": {"coordinates": [-86.806618, 33.415858], "type": "Point"}, "id": "12", "properties": {"Company": "Subway", "Date": "04/14/25", "Name": "SUBWAY #29147  2972 COLUMBIANA RD VESTAVIA HILLS 35216  ", "Permit": 17508, "Score": 99, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.807475, 33.495112, -86.807475, 33.495112], "geometry": {"coordinates": [-86.807475, 33.495112], "type": "Point"}, "id": "13", "properties": {"Company": "Subway", "Date": "03/21/25", "Name": "SUBWAY #27114  1100 12TH ST S BIRMINGHAM 35205  ", "Permit": 25081, "Score": 95, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.694354, 33.593812, -86.694354, 33.593812], "geometry": {"coordinates": [-86.694354, 33.593812], "type": "Point"}, "id": "14", "properties": {"Company": "Subway", "Date": "04/22/25", "Name": "SUBWAY #2018  433 HUFFMAN RD BIRMINGHAM 35215  ", "Permit": 19918, "Score": 91, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.822981, 33.446024, -86.822981, 33.446024], "geometry": {"coordinates": [-86.822981, 33.446024], "type": "Point"}, "id": "15", "properties": {"Company": "Subway", "Date": "04/08/25", "Name": "SUBWAY # 7797  221 LAKESHORE PKWY HOMEWOOD 35209  ", "Permit": 26511, "Score": 94, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.96411, 33.403556, -86.96411, 33.403556], "geometry": {"coordinates": [-86.96411, 33.403556], "type": "Point"}, "id": "16", "properties": {"Company": "Subway", "Date": "03/05/25", "Name": "SUBWAY # 3112  1518 9TH AVE N BESSEMER 35020  ", "Permit": 26519, "Score": 97, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.738758509391, 33.617636730716, -86.738758509391, 33.617636730716], "geometry": {"coordinates": [-86.738758509391, 33.617636730716], "type": "Point"}, "id": "17", "properties": {"Company": "Subway", "Date": "04/04/25", "Name": "SUBWAY - CIRCLE K 2801 PINSON VALLEY PKWY BIRMINGHAM 35217  ", "Permit": 24976, "Score": 91, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "2801 Pinson Valley Pkwy, Birmingham, Alabama, 35217"}, "type": "Feature"}, {"bbox": [-86.787917, 33.480761, -86.787917, 33.480761], "geometry": {"coordinates": [-86.787917, 33.480761], "type": "Point"}, "id": "18", "properties": {"Company": "Subway", "Date": "08/01/25", "Name": "SUBWAY  1919 28TH AVE S HOMEWOOD 35209  ", "Permit": 27277, "Score": 95, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.917683, 33.333751, -86.917683, 33.333751], "geometry": {"coordinates": [-86.917683, 33.333751], "type": "Point"}, "id": "19", "properties": {"Company": "Subway", "Date": "07/14/25", "Name": "SUBWAY  1205 LAKE DR SE BESSEMER 35022  ", "Permit": 27313, "Score": 97, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.806594658032, 33.532009479698, -86.806594658032, 33.532009479698], "geometry": {"coordinates": [-86.806594658032, 33.532009479698], "type": "Point"}, "id": "20", "properties": {"Company": "Subway", "Date": "05/29/25", "Name": "SUBWAY  1219 26TH ST N BIRMINGHAM 35234  ", "Permit": 27518, "Score": 93, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "1219 26th St N, Birmingham, Alabama, 35234"}, "type": "Feature"}, {"bbox": [-86.94176, 33.596278, -86.94176, 33.596278], "geometry": {"coordinates": [-86.94176, 33.596278], "type": "Point"}, "id": "21", "properties": {"Company": "Subway", "Date": "03/05/25", "Name": "SUBWAY  4024 VETERANS MEMORIAL DR ADAMSVILLE 35005  ", "Permit": 27795, "Score": 87, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.924384388572, 33.579546596659, -86.924384388572, 33.579546596659], "geometry": {"coordinates": [-86.924384388572, 33.579546596659], "type": "Point"}, "id": "22", "properties": {"Company": "Subway", "Date": "03/20/25", "Name": "SUBWAY  2473 HACKWORTH RD ADAMSVILLE 35005  ", "Permit": 27796, "Score": 100, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "2473 Hackworth Rd, Birmingham, Alabama, 35214"}, "type": "Feature"}, {"bbox": [-86.958019, 33.490867, -86.958019, 33.490867], "geometry": {"coordinates": [-86.958019, 33.490867], "type": "Point"}, "id": "23", "properties": {"Company": "Subway", "Date": "05/09/25", "Name": "SUBWAY  643 PLEASANT GROVE RD PLEASANT GROVE 35127  ", "Permit": 27931, "Score": 94, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.585592, 33.542552, -86.585592, 33.542552], "geometry": {"coordinates": [-86.585592, 33.542552], "type": "Point"}, "id": "24", "properties": {"Company": "Subway", "Date": "03/13/25", "Name": "SUBWAY  1101 HIGROVE PKWY LEEDS 35094  ", "Permit": 27954, "Score": 97, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.732503, 33.459632, -86.732503, 33.459632], "geometry": {"coordinates": [-86.732503, 33.459632], "type": "Point"}, "id": "25", "properties": {"Company": "Subway", "Date": "07/25/25", "Name": "SUBWAY  3155 GREEN VALLEY RD VESTAVIA HILLS 35243  ", "Permit": 28107, "Score": 89, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.961548, 33.457839, -86.961548, 33.457839], "geometry": {"coordinates": [-86.961548, 33.457839], "type": "Point"}, "id": "26", "properties": {"Company": "Subway", "Date": "07/17/25", "Name": "SUBWAY  810 ALLISON BONNETT MEMORIAL DR HUEYTOWN 35023  ", "Permit": 28339, "Score": 87, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.99927, 33.328199, -86.99927, 33.328199], "geometry": {"coordinates": [-86.99927, 33.328199], "type": "Point"}, "id": "27", "properties": {"Company": "Subway", "Date": "08/22/25", "Name": "SUBWAY  4760 EASTERN VALLEY RD MCCALLA 35111  ", "Permit": 28824, "Score": 97, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.877602, 33.494589, -86.877602, 33.494589], "geometry": {"coordinates": [-86.877602, 33.494589], "type": "Point"}, "id": "28", "properties": {"Company": "Subway", "Date": "06/03/25", "Name": "SUBWAY  2213 BESSEMER RD BIRMINGHAM 35208  ", "Permit": 29004, "Score": 97, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.803336, 33.608445, -86.803336, 33.608445], "geometry": {"coordinates": [-86.803336, 33.608445], "type": "Point"}, "id": "29", "properties": {"Company": "Subway", "Date": "04/28/25", "Name": "SUBWAY  1329 WALKER CHAPEL RD FULTONDALE 35068  ", "Permit": 29112, "Score": 99, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.720244, 33.528925, -86.720244, 33.528925], "geometry": {"coordinates": [-86.720244, 33.528925], "type": "Point"}, "id": "30", "properties": {"Company": "Subway", "Date": "06/03/25", "Name": "SUBWAY  1600 MONTCLAIR RD BIRMINGHAM 35210  ", "Permit": 29134, "Score": 91, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.727616, 33.520856, -86.727616, 33.520856], "geometry": {"coordinates": [-86.727616, 33.520856], "type": "Point"}, "id": "31", "properties": {"Company": "Subway", "Date": "06/03/25", "Name": "SUBWAY  4500 MONTEVALLO RD BIRMINGHAM 35210  ", "Permit": 29135, "Score": 92, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.604725004455, 33.697720995963, -86.604725004455, 33.697720995963], "geometry": {"coordinates": [-86.604725004455, 33.697720995963], "type": "Point"}, "id": "32", "properties": {"Company": "Subway", "Date": "05/20/25", "Name": "SUBWAY  6723 DEERFOOT PKWY CLAY 35126  ", "Permit": 29138, "Score": 91, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "6723 Deerfoot Pkwy, Pinson, Alabama, 35126"}, "type": "Feature"}, {"bbox": [-86.984105, 33.41962, -86.984105, 33.41962], "geometry": {"coordinates": [-86.984105, 33.41962], "type": "Point"}, "id": "33", "properties": {"Company": "Subway", "Date": "05/27/25", "Name": "SUBWAY  2510 19TH ST N HUEYTOWN 35023  ", "Permit": 29174, "Score": 98, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.798758, 33.504644, -86.798758, 33.504644], "geometry": {"coordinates": [-86.798758, 33.504644], "type": "Point"}, "id": "34", "properties": {"Company": "Subway", "Date": "03/11/25", "Name": "SUBWAY  803 20TH ST S BIRMINGHAM 35205  ", "Permit": 26596, "Score": 91, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.810331, 33.524535, -86.810331, 33.524535], "geometry": {"coordinates": [-86.810331, 33.524535], "type": "Point"}, "id": "35", "properties": {"Company": "Subway", "Date": "06/05/25", "Name": "SUBWAY 2105 RICHARD ARRINGTON JR. BLVD N BIRMINGHAM 35203  ", "Permit": 26640, "Score": 100, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.797837, 33.393632, -86.797837, 33.393632], "geometry": {"coordinates": [-86.797837, 33.393632], "type": "Point"}, "id": "36", "properties": {"Company": "Subway", "Date": "03/04/25", "Name": "SUBWAY  3305 LORNA RD HOOVER 35216  ", "Permit": 26772, "Score": 96, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.681625, 33.698409, -86.681625, 33.698409], "geometry": {"coordinates": [-86.681625, 33.698409], "type": "Point"}, "id": "37", "properties": {"Company": "Subway", "Date": "08/25/25", "Name": "SUBWAY  6662 HIGHWAY 75 PINSON 35126  ", "Permit": 26778, "Score": 92, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.847364, 33.497961, -86.847364, 33.497961], "geometry": {"coordinates": [-86.847364, 33.497961], "type": "Point"}, "id": "38", "properties": {"Company": "Subway", "Date": "08/05/25", "Name": "SUBWAY  701 PRINCETON AVE BIRMINGHAM 35211  ", "Permit": 19040, "Score": 100, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.809003, 33.517486, -86.809003, 33.517486], "geometry": {"coordinates": [-86.809003, 33.517486], "type": "Point"}, "id": "39", "properties": {"Company": "Subway", "Date": "05/15/25", "Name": "SUBWAY  1909 5TH AVE N BIRMINGHAM 35203  ", "Permit": 23273, "Score": 95, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.914231, 33.464302, -86.914231, 33.464302], "geometry": {"coordinates": [-86.914231, 33.464302], "type": "Point"}, "id": "40", "properties": {"Company": "Subway", "Date": "03/07/25", "Name": "SUBWAY  133 BESSEMER SUPER HWY MIDFIELD 35228  ", "Permit": 24439, "Score": 92, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.866510029354, 33.349716907064, -86.866510029354, 33.349716907064], "geometry": {"coordinates": [-86.866510029354, 33.349716907064], "type": "Point"}, "id": "41", "properties": {"Company": "Subway", "Date": "06/20/25", "Name": "SUBWAY  2304 JOHN HAWKINS PKWY HOOVER 35244  ", "Permit": 18255, "Score": 95, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "2304 John Hawkins Pkwy, Hoover, Alabama, 35244"}, "type": "Feature"}, {"bbox": [-86.827341, 33.64659, -86.827341, 33.64659], "geometry": {"coordinates": [-86.827341, 33.64659], "type": "Point"}, "id": "42", "properties": {"Company": "Subway", "Date": "05/12/25", "Name": "SUBWAY  841 ODUM RD GARDENDALE 35071  ", "Permit": 22394, "Score": 100, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.74811, 33.52937, -86.74811, 33.52937], "geometry": {"coordinates": [-86.74811, 33.52937], "type": "Point"}, "id": "43", "properties": {"Company": "Subway", "Date": "04/30/25", "Name": "SUBWAY  5506 CRESTWOOD BLVD BIRMINGHAM 35212  ", "Permit": 20617, "Score": 90, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.773423, 33.426274, -86.773423, 33.426274], "geometry": {"coordinates": [-86.773423, 33.426274], "type": "Point"}, "id": "44", "properties": {"Company": "Subway", "Date": "08/01/25", "Name": "SUBWAY  3382 MORGAN DR VESTAVIA HILLS 35216  ", "Permit": 20870, "Score": 99, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Subway"}, "type": "Feature"}, {"bbox": [-86.824368, 33.54187, -86.824368, 33.54187], "geometry": {"coordinates": [-86.824368, 33.54187], "type": "Point"}, "id": "45", "properties": {"Company": "Subway", "Date": "05/06/25", "Name": "CIRCLE K STORE #2709353 - SUBWAY  1901 FINLEY BLVD BIRMINGHAM 35204  ", "Permit": 28285, "Score": 98, "Smoke Free": "Y", "__folium_color": "darkgreen", "address": "Circle K"}, "type": "Feature"}, {"bbox": [-86.643025, 33.5977, -86.643025, 33.5977], "geometry": {"coordinates": [-86.643025, 33.5977], "type": "Point"}, "id": "0", "properties": {"Company": "Firehouse", "Date": "08/27/25", "Name": "FIREHOUSE SUBS  1483 GADSDEN HWY BIRMINGHAM 35235  ", "Permit": 19009, "Score": 94, "Smoke Free": "Y", "__folium_color": "firebrick", "address": "Firehouse Subs"}, "type": "Feature"}, {"bbox": [-86.805633, 33.605199, -86.805633, 33.605199], "geometry": {"coordinates": [-86.805633, 33.605199], "type": "Point"}, "id": "1", "properties": {"Company": "Firehouse", "Date": "07/10/25", "Name": "FIREHOUSE SUBS  3477 LOWERY PKWY FULTONDALE 35068  ", "Permit": 19455, "Score": 99, "Smoke Free": "Y", "__folium_color": "firebrick", "address": "Firehouse Subs"}, "type": "Feature"}, {"bbox": [-86.819461, 33.461212, -86.819461, 33.461212], "geometry": {"coordinates": [-86.819461, 33.461212], "type": "Point"}, "id": "2", "properties": {"Company": "Firehouse", "Date": "05/27/25", "Name": "FIREHOUSE SUBS  808 GREEN SPRINGS HWY HOMEWOOD 35209  ", "Permit": 21863, "Score": 98, "Smoke Free": "Y", "__folium_color": "firebrick", "address": "Firehouse Subs"}, "type": "Feature"}, {"bbox": [-86.988537, 33.333312, -86.988537, 33.333312], "geometry": {"coordinates": [-86.988537, 33.333312], "type": "Point"}, "id": "3", "properties": {"Company": "Firehouse", "Date": "05/29/25", "Name": "FIREHOUSE SUBS  4867 PROMENADE PKWY BESSEMER 35022  ", "Permit": 21981, "Score": 91, "Smoke Free": "Y", "__folium_color": "firebrick", "address": "Firehouse Subs"}, "type": "Feature"}, {"bbox": [-86.80689, 33.404347, -86.80689, 33.404347], "geometry": {"coordinates": [-86.80689, 33.404347], "type": "Point"}, "id": "4", "properties": {"Company": "Firehouse", "Date": "04/01/25", "Name": "FIREHOUSE SUBS  1580 MONTGOMERY HWY HOOVER 35216  ", "Permit": 28189, "Score": 94, "Smoke Free": "Y", "__folium_color": "firebrick", "address": "Firehouse Subs"}, "type": "Feature"}], "type": "FeatureCollection"});
        
                
            
            geo_json_710392236cf02b4b9c99530d1a816795.bindTooltip(
            function(layer){
            let div = L.DomUtil.create('div');
            
            let handleObject = feature => {
                if (feature === null) {
                    return '';
                } else if (typeof(feature)=='object') {
                    return JSON.stringify(feature);
                } else {
                    return feature;
                }
            }
            let fields = ["Permit", "Score"];
            let aliases = ["Permit", "Score"];
            let table = '<table>' +
                String(
                fields.map(
                (v,i)=>
                `<tr>
                    <th>${aliases[i]}</th>
                    
                    <td>${handleObject(layer.feature.properties[v])}</td>
                </tr>`).join(''))
            +'</table>';
            div.innerHTML=table;
            
            return div
            }
            ,{
          "sticky": true,
          "className": "foliumtooltip",
        });
                             
            
            geo_json_710392236cf02b4b9c99530d1a816795.bindPopup(
            function(layer){
            let div = L.DomUtil.create('div');
            
            let handleObject = feature => {
                if (feature === null) {
                    return '';
                } else if (typeof(feature)=='object') {
                    return JSON.stringify(feature);
                } else {
                    return feature;
                }
            }
            let fields = ["address", "Permit", "Score", "Name", "Date", "Smoke Free", "Company"];
            let aliases = ["address", "Permit", "Score", "Name", "Date", "Smoke Free", "Company"];
            let table = '<table>' +
                String(
                fields.map(
                (v,i)=>
                `<tr>
                    <th>${aliases[i].toLocaleString()}</th>
                    
                    <td>${handleObject(layer.feature.properties[v]).toLocaleString()}</td>
                </tr>`).join(''))
            +'</table>';
            div.innerHTML=table;
            
            return div
            }
            ,{
          "className": "foliumpopup",
        });
                             
            
                    geo_json_710392236cf02b4b9c99530d1a816795.addTo(map_67587efcd21f46d2e6582df8c3c5f5ac);
                
        </script>
        </html>
        """

        headers = {"content-type": "text/html;charset=UTF-8"}
        return Response(html, headers=headers)
