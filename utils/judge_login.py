import pytest
import json


class JudgeLogin(object):
    @classmethod
    def judge_main(cls, response, expect_data):
        res = json.loads(response.text)
        assert response.status_code == expect_data['status_code']
        assert res['success'] == expect_data['success']
        assert res['code'] == expect_data['code']
        assert res['message'] in expect_data['message']

