from poca.models import Carpark
from .base import Processor

class CarparkProcessor(Processor):

    def get_model(self):
        return Carpark

    def has_geo(self):
        return True

    def search(self, query, term):
        t = term + "%"
        return query.filter(
            Carpark.county.ilike(t) |
            Carpark.operator.ilike(t) |
            Carpark.name.ilike(t) |
            Carpark.town.ilike(t)
        )

    def get_context(self):
        ''' Return the context for a single result '''
        return {
            'dataset': {
                'title': 'Car Parks'
            },
            'publisher': {'title': 'Multiple Publishers'}
        }

    def is_match(self, terms):
        return 'carpark' in terms or \
            ('car' in terms and 'park' in terms) or \
            ('car' in terms and 'parks' in terms) or \
            'parking' in terms

    def get_search_results(self):
        ''' Assuming a match, get results '''
        results = [
            {
                'title': 'Car Parks',
                'name': 'carparks',
                'description': 'This dataset is an aggregation of the data found in some other datasets ',
                'publisher': {'title': 'Multiple Publishers'},
                'super': True,
            }
        ]

        for name, pub in [('Chester', 'Cheshire West',)]:
            results.append(
                {
                    'title': '{} Car Parks'.format(name),
                    'name': 'carparks_{}'.format(name.lower()),
                    'description': 'Car parks in {}'.format(name),
                    'publisher': {'title': pub},
                    'super': False,
                }
            )
        return results

