import json
import os
import pandas


def load_scores_old(folder : str ='data', all_languages : bool = False):
    """Aggregates stored scores into a table. Excludes languages with 0 scores by default."""
    rows = []
    records = []

    for entry in os.scandir(folder):
        try:
            timestamp = int(entry.name.split('.')[0])
            data = json.load(open(entry.path))
            record = {
                lang['language_string']: lang['points']
                for lang in data['languages'] if all_languages or lang['learning']
            }
            record['Total'] = sum(record.values())

            rows.append(timestamp)
            records.append(record)
        except IOError:
            pass

    return pandas.DataFrame(records, rows).fillna(0).astype(int).sort_index()


def load_scores(folder : str = 'data'):
    def read_file():
        for entry in os.scandir(folder):
            courses = json.load(open(entry.path))['courses']
            crown = {lang['title']: lang['crowns'] for lang in courses}
            xp = {lang['title']: lang['xp'] for lang in courses}
            crown['Total'] = sum(crown.values())
            xp['Total'] = sum(xp.values())
            yield int(entry.name.split('.')[0]), xp, crown

    index, xp, crown = map(list, zip(*read_file()))
    return tuple(pandas.DataFrame(data=x, index=index) for x in (xp, crown))
