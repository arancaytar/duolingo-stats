import requests

def get_data(username):
    return requests.get(f'https://www.duolingo.com/users/{username}').json()

