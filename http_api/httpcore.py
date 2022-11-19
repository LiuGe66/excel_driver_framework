import requests
import json


class CoreHttp:
    def send_http(self, url, param_type, method, data=None, headers=None, **kwargs):
        if param_type == 'json':
            try:
                json.dumps(data, ensure_ascii=False)  # 要求不要把汉字变成ASCII码
                datas = eval(data)
            except Exception as e:
                raise Exception("无法转换为JSON格式，请检查你输入参数")
            response = getattr(requests, method)(url, json=datas, headers=headers, **kwargs)
        elif param_type == 'data':
            response = getattr(requests, method)(url, data=data, headers=headers, **kwargs)
        else:
            response = getattr(requests, method)(url, params=data, headers=headers, **kwargs)
        return response
