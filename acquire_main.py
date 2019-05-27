#!/usr/bin/env python3
import datetime
import json

import acquire

try:
    uid = open('uid.txt').read().strip()
except IOError:
    raise ValueError('Enter your Duolingo user ID in the file `uid.txt`. To discover it, first use `Duolingo.login('
                     'username, password).get_id(username).')
else:
    json.dump(
        acquire.Duolingo.anonymous().get_fields(uid, 'courses'),
        open(f'data/{datetime.datetime.now():%s}.json', 'w')
    )
