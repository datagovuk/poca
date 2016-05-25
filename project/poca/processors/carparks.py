from poca.database import db
from poca.models import Carpark
from .base import Processor

class CarparkProcessor(Processor):

    def noun(self):
        return 'Car Park'

    def noun_plural(self):
        return 'Car Parks'

    def get_model(self):
        return Carpark

    def has_geo(self):
        return True

    def get_geo(self):
        results = []
        res = db.session.query(Carpark.latitude, Carpark.longitude, Carpark.name).all()
        for lat, lng, name in res:
            results.append({
                    'lat': lat, 'lng': lng, 'name': name
                })
        return results

    def search(self, query, term):
        t = term + "%"
        return query.filter(
            Carpark.town.ilike(t)
        )

    def is_match(self, terms):
        return 'carpark' in terms or \
            'carparks' in terms or \
            ('car' in terms and 'park' in terms) or \
            ('car' in terms and 'parks' in terms) or \
            'parking' in terms

    def get_search_results(self):
        ''' Assuming a match, get results '''
        from poca.database import db
        from poca.models import Dataset

        datasets = db.session.query(Dataset)\
            .filter(Dataset.name=='carparks')\
            .order_by(Dataset.is_super.desc())

        return datasets.all()

