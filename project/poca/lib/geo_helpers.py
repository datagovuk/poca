import os
import json
import geojson

from geoalchemy2 import functions, Geometry
from geoalchemy2.elements import WKTElement
from geoalchemy2.functions import GenericFunction

from shapely.geometry import shape


class ST_Force_2D(GenericFunction):
    name = 'ST_Force_2D'
    type = Geometry

def lat_lng_to_geojson(lat, lng):
    return 'POINT({longitude} {latitude})'.format(longitude=lng, latitude=lat)

def geojson_to_wkt(feature, src_srid, dest_srid=4326):
    wkt = WKTElement(shape(geojson.loads(json.dumps(feature))).wkt, src_srid)
    if src_srid != dest_srid:
        wkt = functions.ST_Transform(wkt, dest_srid)

    return ST_Force_2D(wkt)

def geojson_to_centroid_wkt(feature, src_srid, dest_srid=4326):
    wkt = WKTElement(shape(geojson.loads(json.dumps(feature))).centroid.wkt, src_srid)
    if src_srid != dest_srid:
        wkt = functions.ST_Transform(wkt, dest_srid)

    return ST_Force_2D(wkt)

"""
def geom_for_postcode(postcode):
    cp = db.session.query(Codepoint)\
        .filter(Codepoint.postcode==postcode).first()
    if cp:
        return cp.geom
    return None
"""