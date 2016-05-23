import poca.views as v

def create_routes(app):
    app.add_url_rule('/', 'home', v.home)
    app.add_url_rule('/search', 'search', v.search)
    app.add_url_rule('/dataset/<name>', 'dataset', v.dataset)
    app.add_url_rule('/dataset/<name>/data', 'dataset_data', v.dataset_data, methods=['POST'])

