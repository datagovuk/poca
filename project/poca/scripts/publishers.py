"""
Script to load publisher data
"""
import csv
import os
import sys

from flask.ext.script import Command, Option

from poca.models import Publisher
from poca.database import db

class PublisherImport(Command):
    '''Load publisher data '''

    name = "publishers"

    option_list = (
        Option("--inputfile", "-i", dest="inputfile"),
    )

    def run(self, inputfile):
        if not inputfile or not os.path.exists(inputfile):
            print("Missing input folder. Please specify with -i </path/to/csv>")
            return

        reader = csv.reader(open(inputfile, 'r'))
        for row in reader:
            name = row[0]
            title = row[1]
            category = row[2]

            p = (db.session.query(Publisher)
                   .filter(Publisher.name==name).first())
            if not p:
                p = Publisher()

            p.name = name
            p.title = title
            p.category = category

            db.session.add(p)
            db.session.commit()