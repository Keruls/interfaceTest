import config
import requests
import pytest


@pytest.fixture(scope='session')
def get_token():
    res = requests.post(url=config.host+'/api/sys/login',
                        headers={'Content-Type': 'application/json'},
                        json={'mobile': '13800000001', 'password': '123456'}
                        ).json()
    token = config.token + res['data']
    return token
