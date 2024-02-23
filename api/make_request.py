import requests
import config


class SendRequest:
    @classmethod
    def send(cls, http_data):
        if http_data['data_type'] == 'json':
            res = requests.request(method=http_data['method'],
                                   url=config.host + http_data['uri'],
                                   headers=http_data['headers'],
                                   json=http_data.get('data', None),
                                   files=None,
                                   verify=None,
                                   cookies=None,
                                   proxies=config.proxies)
            # 加一个请求后处理方法，根据响应类型json或text，对res进行loads操作，或其他，然后judge去掉loads操作。
            return res
        elif http_data['data_type'] == 'params':
            res = requests.request(method=http_data['method'],
                                   url=config.host + http_data['uri'],
                                   headers=http_data['headers'],
                                   params=http_data.get('data', None),
                                   files=None,
                                   verify=None,
                                   cookies=None,
                                   proxies=config.proxies)
            return res
        elif http_data['data_type'] == 'data':
            res = requests.request(method=http_data['method'],
                                   url=config.host + http_data['uri'],
                                   headers=http_data['headers'],
                                   data=http_data.get('data', None),
                                   files=None,
                                   verify=None,
                                   cookies=None,
                                   proxies=config.proxies)
            return res

    # 方法二
    # @staticmethod
    # def method_get(http_data):
    #     res = requests.get(url=config.host + http_data['uri'],
    #                        headers=http_data['headers'])
    #     return res
    #
    # @staticmethod
    # def method_post(http_data):
    #     res = requests.post(url=config.host + http_data['uri'],
    #                         json=http_data['data'],
    #                         headers=http_data['headers'],
    #                         proxies=config.proxies)
    #     return res
    #
    # @classmethod
    # def send(cls, method, http_data):
    #     if method == 'get':
    #         return cls.method_get(http_data)
    #     elif method == 'post':
    #         return cls.method_post(http_data)
    #     else:
    #         return print('request method error')
