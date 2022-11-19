from time import sleep
from http_api.httpcore import CoreHttp
import jsonpath
from excel_reader.excel_reader import ExcelReader
import pytest
import os


class Test_HttpRun:
    #  定义一个空字典用于接收提取的内容
    contentData = {}
    models = ExcelReader().Read()

    @pytest.mark.parametrize("model", models)
    def test_do_send_http(self, model, **kwargs):  # models是用例条数个对象
        if model.is_need:  # 判断是否需要抽取的值
            if self.contentData:  # 判断字典里有没有东西
                for value in eval(model.need_value):  # model.need_value 是需要提取的key,如:['token']
                    data_value = self.contentData[value]  # 把需要提取的值存入变量data_value
                    model.data = eval(model.data)  # model.data是发请求时带的data数据
                    model.data.update({value: data_value})
            else:
                raise Exception("期望全局变量有结果值，但是没有对应的数据")
        # 请求进行操作 ，发起HTTP请求，进行返回结果断言
        ch = CoreHttp()
        res = ch.send_http(model.url, model.req_type, model.method, model.data, **kwargs)
        # 抽取需要传递给下一个接口的数据
        if model.extract is not None and '' != model.extract:
            for ex in eval(model.extract):  # ['token','id'] type(extract) str  --> token
                j_res = jsonpath.jsonpath(res.json(), '$..' + ex)  # ['xxxxx']
                self.contentData.update({ex: j_res[0]})  # --> token : xxxxx , id: 6 contentData[key]

        # 几个元素 [参数] 外部传递
        if model.assert_options == '包含':
            assert jsonpath.jsonpath(res.json(), '$..' + model.assert_data)
            print("第{}条用例{}断言通过".format(int(model.index), model.desc))
        if model.assert_options == '大于':
            assert res.json()[model.assert_data] > model.assert_value
            print("第{}条用例{}断言通过".format(int(model.index), model.desc))
        if model.assert_options == '小于':
            assert res.json()[model.assert_data] < model.assert_value
            print("第{}条用例{}断言通过".format(int(model.index), model.desc))
        if model.assert_options == '等于':
            assert res.json()[model.assert_data] == model.assert_value
            print("第{}条用例{}断言通过".format(int(model.index), model.desc))


if __name__ == "__main__":
    pytest.main(['-v', '--alluredir', '../report_data', '--clean-alluredir'])
    sleep(3)
    os.system('allure generate ../report_data -o ../report_html/ --clean')


