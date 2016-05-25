"""
A codepoint entry which maps postcode to lat/lng
"""
from poca.database import db

CATEGORIES = {
    "ministerial-department": "Ministerial department",
    "non-ministerial-department": "Non-ministerial department",
    "devolved":  "Devolved administration",
    "executive-ndpb": "Executive non-departmental public body",
    "advisory-ndpb":  "Advisory non-departmental public body",
    "tribunal-ndpb":  "Tribunal non-departmental public body",
    "executive-agency": "Executive agency",
      "executive-office": "Executive office",
    "local-council": "Local authority",
    "nhs": "NHS body",
    "gov-corporation": "Public corporation",
    "charity-ngo": "Charity or Non-Governmental Organisation",
    "private": "Private Sector",
    "grouping": "A notional grouping of organisations",
    "sub-organisation": "Sub-organisation",
    "other": "Other",
}

class Publisher(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.Unicode(), nullable=False, index=True)
    title = db.Column(db.Unicode())
    category = db.Column(db.Unicode())

    datasets = db.relationship('Dataset', backref='publisher',
                                lazy='dynamic')
