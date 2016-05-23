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
    from poca.database import db
    from poca.processors import get_processor_by_name
    p = get_processor_by_name(name)
    ctx = p.get_context()
    ctx['_has_geo'] = p.has_geo()

    f = db.session.query(p.get_model()).first()
    ctx['_columns'] = f.get_columns()

    return render_template('dataset.html', **ctx)

def dataset_data(name):
    ''' Lookup processor and details by name '''
    from poca.processors import get_processor_by_name
    p = get_processor_by_name(name)
    m = p.get_model()

    from pprint import pprint
    pprint(request.args)

    draw = int(request.args.get('draw', 1))
    offset = int(request.args.get('start', 0))
    limit = int(request.args.get('length', 10))

    data = db.session.query(m).offset(offset).limit(limit)
    count = db.session.query(m).count()

    results = {
        'draw': draw,
        'recordsFiltered': count,
        'recordsTotal': count,
        'data': [d.to_dict() for d in data]
    }

    return jsonify(results)

