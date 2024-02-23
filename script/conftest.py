# 管理一个package下的所有fixture，比如所有测试都需要用到获取token的fixture时，将该fixture放到此文件下
# 用例文件下无需import conftest
# 他的作用范围是在当前目录下所有的测试模块。
import pytest
import requests
import config


# 获取鉴权码
@pytest.fixture(scope='session')
def get_token():
    res = requests.post(url=config.host+'/api/sys/login',
                        headers={'Content-Type': 'application/json'},
                        json={'mobile': '13800000001', 'password': '123456'}
                        ).json()
    config.token[0] = config.token[0] + res['data']
    print(config.token[0])
