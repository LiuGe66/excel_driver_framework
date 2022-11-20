import requests
from Utils.logger_utils import print_log


class CoreHttp:
    sess = requests.session()

    def send_http(self, method, url, params=None, json=None, headers=None, data=None):
        # print_log("请求方法是：%s" % (method))
        # print("这也不行吗")
        # print_log("请求地址是：{}".format(url))
        # if params:
        #     print_log("请求params是：{}".format(params))
        # if json:
        #     print_log("请求josn是：{}".format(json))
        # if headers:
        #     print_log("请求headers是：{}".format(headers))
        # if data:
        #     print_log("请求data是：{}".format(data))
        response = CoreHttp().sess.request(method, url, params=params, data=data, headers=headers, json=json)
        return response



if __name__ == '__main__':
    c = CoreHttp()
