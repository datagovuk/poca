from poca.database import db
from poca.models import Spend
from .base import Processor

class SpendProcessor(Processor):

    def noun(self):
        return 'Spend Data'

    def noun_plural(self):
        return 'Spend Data'

    def get_model(self):
        return Spend

    def has_geo(self):
        return False

    def get_geo(self):
        return None

    def search(self, query, term):
        t = term + "%"
        return query.filter(
            Spend.BeneficiaryName.ilike(t)
            | (Spend.OrganisationalUnit.ilike(t))
        )

    def is_match(self, terms):
        return 'spend' in terms or \
            'spending' in terms

    def get_search_results(self):
        ''' Assuming a match, get results '''
        from poca.database import db
        from poca.models import Dataset

        datasets = db.session.query(Dataset)\
            .filter(Dataset.name=='spend')\
            .order_by(Dataset.is_super.desc())

        return datasets.all()

