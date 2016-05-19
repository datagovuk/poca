import poca.views as v

def create_routes(app):
    app.add_url_rule('/', 'home', v.home)

