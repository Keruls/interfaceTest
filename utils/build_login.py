import config
import os
import json as j


class BuildLogin:
    url = config.host + '/api/sys/login'
    headers = {'Content-Type': 'application/json'}
    f_path = os.path.dirname(os.path.dirname(__file__)) + '/data/login_test_data.json'
    # 获取请求所需数据,断言所需数据
    @classmethod
    def get_data(cls):
        data_list = []
        with open(cls.f_path, mode='r', encoding='utf-8') as f:
            case_data = j.load(f)
            # f.seek(0)
            # print(f.read())
            for c in case_data:
                case_title = c.get('desc')
                json = c.get('login_data')
                status_code = c.get('status_code')
                success = c.get('success')
                code = c.get('code')
                message = c.get('message')
                # [(c_t,{ },{ })]
                data_list.append((
                    case_title,
                    dict(url=cls.url,  headers=cls.headers, json=json),
                    dict(status_code=status_code, success=success, code=code, message=message)
                ))
            # print(data_list)
            return data_list
