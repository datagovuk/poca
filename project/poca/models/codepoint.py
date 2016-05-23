"""
A codepoint entry which maps postcode to lat/lng
"""
from poca.database import db

from geoalchemy2 import Geography
from geoalchemy2.shape import to_shape


class Codepoint(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    postcode = db.Column(db.Unicode(), nullable=False, index=True)
    quality = db.Column(db.Unicode())
    country = db.Column(db.Unicode())
    nhs_region = db.Column(db.Unicode())
    nhs_authority = db.Column(db.Unicode())
    county = db.Column(db.Unicode())
    district = db.Column(db.Unicode())
    ward = db.Column(db.Unicode())
    geom = db.Column(Geography(spatial_index=False))

    @property
    def lat(self):
        return to_shape(self.geom).y

    @property
    def lon(self):
        return to_shape(self.geom).x

