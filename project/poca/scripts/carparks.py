"""
Script to load carpark data
"""
import csv
import os
import sys

from flask.ext.script import Command, Option
from geojson import Point

from poca.models import Carpark
from poca.database import db
from poca.lib.geo_helpers import lat_lng_to_geojson


class CarparkImport(Command):
    '''Load carpark data '''

    name = "carparks"

    option_list = (
        Option("--inputfile", "-i", dest="inputfile"),
    )

    def run(self, inputfile):
        if not inputfile or not os.path.exists(inputfile):
            print("Missing input folder. Please specify with -i </path/to/csv>")
            return

        reader = csv.DictReader(open(inputfile, 'r'))
        for row in reader:

            try:
                float(row['Lat'])
            except:
                print("Skipping {} as has no lat/lng".format(row.get('Car Park Name')))
                continue

            auto_id = int(row.get('autoID'))
            c = (db.session.query(Carpark)
                   .filter(Carpark.auto_id==auto_id).first())
            if not c:
                c = Carpark()

            c.auto_id = row.get('autoID')
            c.name = row.get('Car Park Name')
            c.operator = row.get('Car Park Operator')
            c.scheme_status = row.get('Scheme Status')
            c.part_time_award = row.get('Part Time Award')
            c.phone = row.get('Car Park Phone')
            c.street_1 = row.get('Street 1')
            c.street_2 = row.get('Street 2')
            c.street_3 = row.get('Street 3')
            c.town = row.get('Town')
            c.county  = row.get('County')
            c.postcode  = row.get('Postcode')
            c.physical_type  = row.get('Physical Type')
            c.payment_type  = row.get('Payment Type')
            c.number_of_spaces  = int(row.get('Number of Spaces', 0))
            c.disabled_spaces  = int(row.get('Disabled Spaces', 0))
            c.cycles  = row.get('Cycles')
            c.motobike  = row.get('Motobike')
            c.cars  = row.get('Cars')
            c.bus  = row.get('Bus')
            c.coach  = row.get('Coach')
            c.truck_parking_area  = row.get('Truck Parking Area')

            c.longitude  = row.get('Long')
            c.latitude  = row.get('Lat')
            c.point = lat_lng_to_geojson(c.latitude, c.longitude)

            db.session.add(c)
            db.session.commit()