


class Processor(object):

    def noun(self):
        return 'Thing'

    def noun_plural(self):
        return 'Things'

    def is_match(self, terms):
        return True

    def get_search_results(self):
        return []

    def has_geo(self):
        return False


    def search(self, query, term):
        return query

    def get_geo(self):
        return []