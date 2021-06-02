Network analysis on own design
==============================

The blueprint for the structural changes of the to-be-developed area was exported as a raster graphic, and uploaded to the tile server [mapwarper.net](https://mapwarper.net/).
The tiles were then loaded into the OpenStreetMap iD editor, and traced to generate an opsntreet map change file [changes.osc](changes.osc).

Download Area data
------------------

```
mkdir overpass_db/
wget -O westbahnhof.osm https://overpass-api.de/api/map?bbox=16.3029,48.1800,16.3490,48.2043
```

Apply changes
-------------

```
<westbahnhof.osm osmchange64 changes.osc  > westbahnhof_changed.osm
sed -i 's/id="-/id="/g' westbahnhof_changed.osm
sed -i 's/ref="-/ref="/g' westbahnhof_changed.osm
```

or:

```
cp changes.osc overpass_db/changes.osc
sed -i 's/id="-/id="/g' overpass_db/changes.osc
sed -i 's/ref="-/ref="/g' overpass_db/changes.osc
python xapi_attr.py overpass_db/changes.osc
osmosis  --read-xml-change file="overpass_db/changes_attr.osc" --sort-change --simplify-change --write-xml-change file="overpass_db/changes_simplified.osc"
osmosis  --read-xml-change file="overpass_db/changes_simplified.osc" --read-xml file="westbahnhof.osm" --apply-change --write-xml file="overpass_db/westbahnhof_changed.osm"
```

```
bzip2 overpass_db/westbahnhof_changed.osm
```

Start Overpass API server
-------------------------

```
docker run \
  -e OVERPASS_META=yes \
  -e OVERPASS_MODE=init \
  -e OVERPASS_PLANET_URL=file:///db/westbahnhof_changed.osm.bz2 \
  -e OVERPASS_RULES_LOAD=1 \
  -e OVERPASS_RATE_LIMIT=10 \
  -v ${PWD}/overpass_db/:/db \
  -p 12345:80 \
  -i -t \
  --name overpass_westbahnhof wiktorn/overpass-api

docker start overpass_westbahnhof
```

Cleanup
-------

```
docker stop overpass_westbahnhof; docker rm overpass_westbahnhof; rm -rf overpass_db/
```
