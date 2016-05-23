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

from poca.database import db

logger = logging.getLogger(__name__)

def home():
    ctx = {}
    return render_template('index.html', **ctx)

def search():
    from poca.processors import get_processors

    terms = request.args.get('q', '')
    lowered = [t.lower() for t in terms.split(' ')]

    for proc in get_processors():
        p = proc()
        if p.is_match(lowered):
            results = p.get_search_results()
            ctx = {
              'terms': terms,
              'results': results,
            }
            break

    return render_template('search.html', **ctx)

def dataset(name):
    ''' Lookup processor and details by name '''
    from poca.processors import get_processor_by_name
    p = get_processor_by_name(name)
    ctx = p.get_context()
    ctx['_has_geo'] = p.has_geo()
    return render_template('dataset.html', **ctx)

def dataset_data(name):
    ''' Lookup processor and details by name '''
    from poca.processors import get_processor_by_name
    p = get_processor_by_name(name)
    m = p.get_model()

    page = 1
    try:
        page = int(request.args.get('page', 1))
    except:
        page = 1

    per_page = 50
    offset = (per_page * page) - per_page

    data = db.session.query(m).offset(offset).limit(per_page)
    results = {
        'total': db.session.query(m).count(),
        'data': [d.to_dict() for d in data]
    }
    return jsonify(results)

