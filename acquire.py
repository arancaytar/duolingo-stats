import requests
import json


class Duolingo:
    jwt: str
    session: requests.Session

    def __init__(self, jwt: str, session: requests.Session):
        self.jwt = jwt
        self.session = session

    @classmethod
    def login(cls, user: str, password: str) -> 'Duolingo':
        session = requests.Session()
        req = requests.post(
            'https://www.duolingo.com/login',
            json={'login': user, 'password': password},
            cookies=session.cookies
        )
        if req.json().get('response') == 'OK':
            return cls(req.headers['jwt'], session)
        else:
            raise ValueError(json.dumps(req.json()))

    @classmethod
    def anonymous(cls) -> 'Duolingo':
        return cls('', requests.Session())

    def assert_logged_in(self):
        assert self.jwt, 'Cannot perform restricted action without authentication.'

    def get_data_extended(self, username: str) -> dict:
        self.assert_logged_in()
        return requests.get(
            f'https://www.duolingo.com/users/{username}',
            headers={'Authorization': f'Bearer {self.jwt}'},
            cookies=self.session.cookies
        ).json()

    def get_id(self, username: str) -> int:
        return self.get_data_extended(username)['id']

    def get_fields(self, uid: int, *fields: str) -> dict:
        return requests.get(
            # this one is still anonymously available.
            f'https://www.duolingo.com/2017-06-30/users/{uid}',
            params={'fields': ','.join(fields) or None},
            cookies=self.session.cookies
        ).json()

    def save(self, filename: str) -> None:
        open(filename, 'w').write(self.jwt)

    @classmethod
    def load(cls, filename: str) -> 'Duolingo':
        return cls(open(filename).read(), requests.Session())
