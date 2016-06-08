'''
Handle the datatable parameters to modify a SQL query
'''

def get_sort(input_dict):
    col = input_dict.get('order[0][column]', '')
    if not col:
        return None

    key = 'columns[{}][data]'.format(col)
    fieldname = input_dict.get(key)
    if not fieldname:
        return None

    order = input_dict.get('order[0][dir]')
    if not order:
        return None

    return '"{}" {}'.format(fieldname, order)
