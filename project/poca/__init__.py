from flask import Flask

from poca.database import db
from poca.routes import create_routes

import poca.models

app = Flask(__name__)
app.config.from_object("poca.config.DevelopmentConfig")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
db.init_app(app)

create_routes(app)

