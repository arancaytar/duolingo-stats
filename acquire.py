import datetime
import requests

username = open('username.txt').read().strip()
data = requests.get(f'https://www.duolingo.com/users/{username}').content
destination = f'data/{datetime.datetime.now():%s}.json'
open(destination, 'wb').write(data)
