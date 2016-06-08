"""
Script to load spend data
"""
import csv
import os
import sys

from flask.ext.script import Command, Option

from poca.models import Spend
from poca.database import db


class SpendImport(Command):
    '''Load spend data '''

    name = "spend"

    option_list = (
        Option("--inputfile", "-i", dest="inputfile"),
    )

    def run(self, inputfile):
        if not inputfile or not os.path.exists(inputfile):
            print("Missing input folder. Please specify with -i </path/to/csv>")
            return

        reader = csv.DictReader(open(inputfile, 'r'))
        for row in reader:

            OrganisationLabel = row.get('OrganisationLabel')
            OrganisationalUnit = row.get('OrganisationalUnit')
            TransactionNumber = row.get('TransactionNumber')
            BeneficiaryName = row.get('BeneficiaryName')
            ExpenseType = row.get('ExpenseType')
            PaymentDate = row.get('PaymentDate')
            Amount = float(row.get('Amount'))

            if not OrganisationalUnit:
                continue
            if Amount == 0.0:
                continue

            s = (db.session.query(Spend)
                   .filter(Spend.OrganisationLabel==OrganisationLabel)\
                   .filter(Spend.PaymentDate==PaymentDate)\
                   .filter(Spend.Amount==Amount).first())
            if not s:
                s = Spend()

            s.OrganisationLabel = OrganisationLabel
            s.OrganisationalUnit = OrganisationalUnit
            s.TransactionNumber = TransactionNumber
            s.BeneficiaryName = BeneficiaryName
            s.ExpenseType = ExpenseType
            s.PaymentDate = PaymentDate
            s.Amount = Amount

            db.session.add(s)
            db.session.commit()
