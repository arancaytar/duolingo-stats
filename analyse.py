import json
import os
import pandas


def load_data():
    columns = set()
    rows = []
    records = []

    for name in os.listdir('data'):
        data = json.load(open(f'data/{name}'))
        record = {lang['language_string']: lang['points'] for lang in data['languages']}
        timestamp = int(name.split('.')[0])

        records.append(record)
        rows.append(timestamp)

    return pandas.DataFrame(records, rows)
