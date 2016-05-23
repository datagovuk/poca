# autoID,Car Park Name,Car Park Operator,Scheme Status,Part Time Award,Car Park Phone,Street 1,Street 2,Street 3,Town,County,Postcode,Physical Type,Payment Type,Number of Spaces,Disabled Spaces,Cycles,Motobike,Cars,Bus,Coach,Truck Parking Area,Monday Open,Monday Close,Monday 24,Monday Closed,Tuesday Open,Tuesday Close,Tuesday 24,Tuesday Closed,Wednesday Open,Wednesday Close,Wednesday 24,Wednesday Closed,Thursday Open,Thursday Close,Thursday 24,Thursday Closed,Friday Open,Friday Close,Friday 24,Friday Closed,Saturday Open,Saturday Close,Saturday 24,Saturday Closed,Sunday Open,Sunday Close,Sunday 24,Sunday Closed,Keywords,Long,Lat

from poca.database import db

from geoalchemy2 import Geography
from geoalchemy2.shape import to_shape

class Carpark(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    auto_id = db.Column(db.Integer())
    name = db.Column(db.Unicode())
    operator = db.Column(db.Unicode())
    scheme_status = db.Column(db.Unicode())
    part_time_award = db.Column(db.Unicode())
    phone = db.Column(db.Unicode())
    street_1 = db.Column(db.Unicode())
    street_2 = db.Column(db.Unicode())
    street_3 = db.Column(db.Unicode())
    town = db.Column(db.Unicode())
    county  = db.Column(db.Unicode())
    postcode  = db.Column(db.Unicode())
    physical_type  = db.Column(db.Unicode())
    payment_type  = db.Column(db.Unicode())
    number_of_spaces  = db.Column(db.Integer())
    disabled_spaces  = db.Column(db.Integer())
    cycles  = db.Column(db.Unicode())
    motobike  = db.Column(db.Unicode())
    cars  = db.Column(db.Unicode())
    bus  = db.Column(db.Unicode())
    coach  = db.Column(db.Unicode())
    truck_parking_area  = db.Column(db.Unicode())

    longitude  = db.Column(db.Unicode())
    latitude  = db.Column(db.Unicode())
    point = db.Column(Geography('POINT', spatial_index=False))

    def to_dict(self):
        return {k:self.__dict__[k] for k in sorted(self.__dict__) if '_sa_' != k[:4] and not k == 'point'}

    #Monday Open,Monday Close,Monday 24,Monday Closed,Tuesday Open,Tuesday Close,Tuesday 24,Tuesday Closed,Wednesday Open,Wednesday Close,Wednesday 24,Wednesday Closed,Thursday Open,Thursday Close,Thursday 24,Thursday Closed,Friday Open,Friday Close,Friday 24,Friday Closed,Saturday Open,Saturday Close,Saturday 24,Saturday Closed,Sunday Open,Sunday Close,Sunday 24,Sunday Closed,Keywords,

