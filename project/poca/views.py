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
import re
import logging

from poca.database import db

logger = logging.getLogger(__name__)

PLACE_MATCH = re.compile('.* in (.*)')

def home():
    ctx = {}
    return render_template('index.html', **ctx)

def search():
    from poca.processors import get_processors

    terms = request.args.get('q', '').strip()
    lowered = [t.lower() for t in terms.strip().split(' ')]

    m = PLACE_MATCH.match(terms)
    if m:
        location = m.groups(0)[0]
        location = location[0].upper() + location[1:].lower()
    else:
        location = ''

    for proc in get_processors():
        p = proc()
        if p.is_match(lowered):
            results = p.get_search_results()
            ctx = {
              'terms': terms,
              'results': results,
              'location': location
            }
            break

    return render_template('search.html', **ctx)

def dataset(publisher_name, name):
    ''' Lookup processor and details by name '''
    from poca.database import db
    from poca.models import Publisher, Dataset
    from poca.processors import get_processor_by_name

    publisher = db.session.query(Publisher)\
        .filter(Publisher.name == publisher_name).first()
    if not publisher:
        abort(404)

    dataset = db.session.query(Dataset)\
        .filter(Dataset.name==name)\
        .filter(Dataset.publisher_id==publisher.id).first()
    if not dataset:
        abort(404)

    p = get_processor_by_name(name)
    f = db.session.query(p.get_model()).first()

    ctx = {
        'dataset': dataset,
        '_has_geo': p.has_geo(),
        'q': request.args.get('q', ''),
        '_columns': f.get_columns(),
    }

    return render_template('dataset.html', **ctx)

def dataset_geo(name):
    from poca.processors import get_processor_by_name
    p = get_processor_by_name(name)
    geo = p.get_geo()
    res = {
      'points': geo
    }
    return jsonify(res)

def dataset_data(name):
    ''' Lookup processor and details by name '''
    from poca.lib.data_filters import get_sort
    from poca.processors import get_processor_by_name
    p = get_processor_by_name(name)
    m = p.get_model()

    draw = int(request.form.get('draw', 1))
    offset = int(request.form.get('start', 0))
    limit = int(request.form.get('length', 10))

    query = db.session.query(m)
    search = request.form.get('search[value]', '')
    if search:
        query = p.search(query, search)

    sort = get_sort(request.form)
    if sort:
        print(sort)
        data = query.order_by(sort).offset(offset).limit(limit)
    else:
        data = query.offset(offset).limit(limit)
    total = db.session.query(m).count()

    results = {
        'draw': draw,
        'recordsFiltered': query.count(),
        'recordsTotal': total,
        'data': [d.to_dict() for d in data]
    }

    return jsonify(results)

