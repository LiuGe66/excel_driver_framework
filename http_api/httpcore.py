import requests
from Utils.logger_utils import print_log


class CoreHttp:
    sess = requests.session()

    def send_http(self, method, url, params=None, json=None, headers=None, data=None):
        # print_log("���󷽷��ǣ�%s" % (method))
        # print("��Ҳ������")
        # print_log("�����ַ�ǣ�{}".format(url))
        # if params:
        #     print_log("����params�ǣ�{}".format(params))
        # if json:
        #     print_log("����josn�ǣ�{}".format(json))
        # if headers:
        #     print_log("����headers�ǣ�{}".format(headers))
        # if data:
        #     print_log("����data�ǣ�{}".format(data))
        response = CoreHttp().sess.request(method, url, params=params, data=data, headers=headers, json=json)
        return response



if __name__ == '__main__':
    c = CoreHttp()
