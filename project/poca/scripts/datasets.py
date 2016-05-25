"""
Script to load dataset data
"""
import json
import os
import sys

from flask.ext.script import Command, Option

from poca.models import Publisher, Dataset
from poca.database import db

class DatasetImport(Command):
    '''Load dataset data '''

    name = "datasets"

    option_list = (
        Option("--inputfile", "-i", dest="inputfile"),
    )

    def run(self, inputfile):
        if not inputfile or not os.path.exists(inputfile):
            print("Missing input folder. Please specify with -i </path/to/csv>")
            return

        items = json.load(open(inputfile, 'r'))
        for row in items:
            name = row['name']
            title = row['title']
            description = row['description']
            publisher_id = row['publisher_id']
            is_super = row['is_super']

            d = (db.session.query(Dataset)
                   .filter(Dataset.name==name)\
                   .filter(Dataset.publisher_id==publisher_id).first())
            if not d:
                d = Dataset()

            d.name = name
            d.title = title
            d.description = description
            d.publisher_id = publisher_id
            d.is_super = is_super

            db.session.add(d)
            db.session.commit()