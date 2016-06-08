import locale
from poca.database import db


class Spend(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    OrganisationLabel = db.Column(db.Unicode())
    OrganisationalUnit = db.Column(db.Unicode())
    TransactionNumber = db.Column(db.Unicode())
    BeneficiaryName = db.Column(db.Unicode())
    ExpenseType = db.Column(db.Unicode())
    PaymentDate = db.Column(db.Unicode())
    Amount = db.Column(db.Float())

    def get_columns(self):
        return [
            "OrganisationLabel",
            "OrganisationalUnit",
            #"TransactionNumber",
            "BeneficiaryName",
            "ExpenseType",
            "PaymentDate",
            "Amount",
        ]

    def to_dict(self):
        data = {k:self.__dict__[k] for k in sorted(self.__dict__) if '_sa_' != k[:4] and not k == 'point'}
        data['Amount'] = '{:20,.2f}'.format(data['Amount'])
        return data

