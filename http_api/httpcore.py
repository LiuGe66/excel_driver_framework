import requests
from Utils.logger_utils import print_log


class CoreHttp:
    sess = requests.session()

    def send_http(self, method, url, params=None, json=None, headers=None, data=None):
        print_log("请求的方法是：{}".format(method))
        print_log("请求的地址是：{}".format(url))
        if params:
            print_log("请求的params是{}".format(params))
        if json:
            print_log("请求的json是{}".format(json))
        if headers:
            print_log("请求的headers是{}".format(headers))
        if data:
            print_log("请求的data是{}".format(data))
        response = CoreHttp.sess.request(method, url, params=params, data=data, headers=headers, json=json)
        print_log("响应数据是：{}".format(response.text))
        return response
