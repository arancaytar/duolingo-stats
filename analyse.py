import json
import os
import pandas


def load_scores(all_languages=False):
    """Aggregates stored scores into a table. Excludes languages with 0 scores by default."""
    rows = []
    records = []

    for entry in os.scandir('data'):
        try:
            timestamp = int(entry.name.split('.')[0])
            data = json.load(open(entry.path))
            record = {lang['language_string']: lang['points'] for lang in data['languages'] if all_languages or lang['learning']}

            rows.append(timestamp)
            records.append(record)
        except:
            pass

    return pandas.DataFrame(records, rows)
