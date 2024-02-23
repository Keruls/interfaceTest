import pytest
import config
from api.make_request import SendRequest
from utils.judge_login import JudgeLogin
from utils.excel_handle import ExcelHandle


# 获取测试用例数据
def get_list():
    data_list = ExcelHandle('login')
    return data_list


@pytest.mark.usefixtures("get_token")
class TestLogin(object):
    @pytest.fixture(scope='class')
    def init_test(self):
        return JudgeLogin()

    @pytest.mark.parametrize('data', get_list().get_data())
    def test_main(self, data, init_test):
        # 请求头添加鉴权码
        data['headers']['Authorization'] = config.token[0]
        # 发送请求
        res = SendRequest.send(data)
        # 断言
        init_test.judge_main(res, data['expect'])
