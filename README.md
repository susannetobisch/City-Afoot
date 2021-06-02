City Afoot
==========

[City Isochrone](City%20Isochrone.ipynb)
--------------------------------------

Isochrone walking Maps - three different types of illustration

<p align="left">
  <img src="/figures/city_isochrone_dots.png" width="30%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="/figures/city_isochrone_polygones.png" width="30%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="/figures/city_isochrone_buffer.png" width="30%">
</p>

[Isochrones](Isochrones.ipynb)
------------------------------

How far can I walk in 1, 5, 10, 15 and 20 minutes, starting from a specified point?
This can indicate irregularities in the urban structure. 

<p align="left">
  <img src="/figures/isochrones.png" width="40%">
</p>

[Network Density](Network%20Density.ipynb)
----------------------------------------

Show different Networks and their basic stats (of particular interest for this project is the street density)

<p align="left">
  <img src="/figures/network_density_simplified_1010.png" width="30%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="/figures/network_density_simplified_1070.png" width="30%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="/figures/network_density_simplified_1150.png" width="30%">
</p>

[POI Maps](POI%20Maps.ipynb)
--------------------------

Map Points of Interest onto a Street Network

*Citybike stations:*

<p align="left">
  <img src="/figures/pois_citybike.png" width="40%">
</p>

[Square Mile](Square%20Mile.ipynb)
--------------------------------

Street Network Figure-Ground Diagrams

<p align="left">
  <img src="/figures/square_mile_stephansplatz.png" width="22%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="/figures/square_mile_wilhelminenstrasse.png" width="22%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="/figures/square_mile_himmelstrasse.png" width="22%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="/figures/square_mile_hlawkagasse.png" width="22%">
</p>

[Structure Isodistance](Structure%20Isodistance.ipynb)
----------------------------------------------------

Structure Isodistance Comparison to Areal Distance

Show the permeability of different street network types by comparing actual reach to areal distance

<p align="left">
  <img src="/figures/structure_hoher_markt.png" width="30%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="/figures/structure_wilhelminenstrasse.png" width="30%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="/figures/structure_himmelstrasse.png" width="30%">
</p>

<p align="left">
  <img src="/figures/structure_sievering.png" width="30%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="/figures/structure_ballard.png" width="30%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="/figures/structure_lake_forest_park.png" width="30%">
</p>


[Stops Isodistance](Stops%20Isodistance.ipynb)
--------------------------------------------

Map Stations of the Public Transport System onto a Street Network and create an Isodistance Map to show the coverage of the Public Transport System

*Status quo:*

<p align="left">
  <img src="/figures/stops_subway_points.png" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="/figures/stops_subway_isodistance.png" width="45%">
</p>

<p align="left">
  <img src="/figures/stops_all_points.png" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="/figures/stops_all_isodistance.png" width="45%">
</p>

*Own design:*

<p align="left">
  <img src="/figures/stops_design_subway_points.png" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="/figures/stops_design_subway_isodistance.png" width="45%">
</p>

<p align="left">
  <img src="/figures/stops_design_all_points.png" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="/figures/stops_design_all_isodistance.png" width="45%">
</p>


[Street Network Design](Street%20Network%20Design.ipynb)
----------------------------------------------------

<p align="left">
  <img src="/figures/street_network_ped.png" width="45%">
&nbsp; &nbsp; &nbsp; &nbsp;
  <img src="/figures/street_network_mit.png" width="45%">
</p>

[Centrality Betweenness](Centrality%20Betweenness.ipynb)
------------------------------------------------------

<p align="left">
  <img src="/figures/centrality_betweenness.png" width="40%">
</p>

[Debug Matplotlib](Debug%20Matplotlib.ipynb)
--------------------------------------------

was used for troubleshooting the data of the street network.
It provides an interactive matplotlib widget, which shows details like street name and length, upon clicking on edges of the displayed graph.

Incorporating own blueprint for Westbahnhof area
------------------------------------------------

Part of the work was to design a walkable urban structure and implement it into the area.

Changes were performed on the existing area in OpenStreetMap via the iD editor, and then downloaded as change-set (.osc) file.
Based on this, an Overpass API server, available under `http://127.0.0.1:12345/api` was started - details to that can be found in the [osm](osm) folder. 
