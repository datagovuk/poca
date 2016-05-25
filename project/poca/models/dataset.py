"""
A dataset entry which maps postcode to lat/lng
"""
from poca.database import db


class Dataset(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Unicode(), nullable=False, index=True)
    title = db.Column(db.Unicode())
    description = db.Column(db.Unicode())

    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))

    issue_date  = db.Column(db.Unicode())
    update_date = db.Column(db.Unicode())
    next_update_date = db.Column(db.Unicode())
    theme = db.Column(db.Unicode())

    temporal_coverage = db.Column(db.Unicode())
    schema = db.Column(db.Unicode())

    is_super = db.Column(db.Boolean())
