from flask import (render_template,
                   request,
                   session,
                   abort,
                   flash,
                   redirect,
                   url_for,
                   current_app,
                   jsonify)

import json
import logging

logger = logging.getLogger(__name__)


def home():
    ctx = {}
    return render_template('index.html', **ctx)

