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

def search():
  terms = request.args.get('q', '')
  results = [
    {'title': 'My shiny dataset',
      'description': 'This dataset is an aggregation of the data found in some other datasets ',
      'publisher': {'title': 'Cabinet Office'}
    },
    {'title': 'Another shiny dataset',
     'description': 'There is very little data in this dataset, in fact it is a PDF file!',
      'publisher': {'title': 'Cabinet Office'}
    },
  ]

  ctx = {
    'terms': terms,
    'results': results,
  }
  return render_template('search.html', **ctx)