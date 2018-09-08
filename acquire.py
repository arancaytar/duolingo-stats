import datetime
import requests

try:
    username = open('username.txt').read().strip()
except:
    raise ValueError('Enter your Duolingo username in the file `username.txt`.')

data = requests.get(f'https://www.duolingo.com/users/{username}').content
destination = f'data/{datetime.datetime.now():%s}.json'
open(destination, 'wb').write(data)
