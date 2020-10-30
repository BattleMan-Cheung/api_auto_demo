import requests

from json import JSONDecodeError


class RequestsHandler:

    def __init__(self):
        self.session = requests.Session()

    def visit(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        res = self.session.request(method, url, params=params, data=data, json=json, headers=headers, **kwargs)

        try:
            return res.json()
        except JSONDecodeError:
            return 'Not Json!'

    def close_session(self):
        self.session.close()


if __name__ == '__main__':
    req = RequestsHandler()

    result = req.visit('post', 'http://127.0.0.1:5000/login', data='zxc')

    print(result)
