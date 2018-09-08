import json
import os
import pandas


def load_data():
    columns = set()
    rows = []
    records = []
    for name in os.listdir('data'):
        timestamp = int(name.split('.')[0])
        data = json.load(open(f'data/{name}'))
        record = {x['language_string']: x['points'] for x in data['languages']}
        rows.append(timestamp)
        columns |= record.keys()
        records.append(record)

    return pandas.DataFrame(records, rows, columns)
