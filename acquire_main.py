#!/usr/bin/env python3
import datetime
import json

import acquire

try:
    username = open('username.txt').read().strip()
    json.dump(
        {'languages': acquire.get_data(username)['languages']},
        open(f'data/{datetime.datetime.now():%s}.json', 'w')
    )
except:
    raise ValueError('Enter your Duolingo username in the file `username.txt`.')
