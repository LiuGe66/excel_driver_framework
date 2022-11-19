import xlrd2
from http_model.http_model import Model


class ExcelReader:
    def Read(self):
        reader = xlrd2.open_workbook(r'..\data\case.xlsx')  # 创建excel对象
        sheet_names = reader.sheet_names()  # 获取所有sheet名
        models = []
        # 在sheet页中循环
        for name in sheet_names:
            #  定义sheet页变量并赋值
            sheet_name = reader.sheet_by_name(name)
            for i in range(sheet_name.nrows):
                if i == 0 or i == 1:  # 跳过前两行
                    continue
                data_list = []
                for j in range(sheet_name.ncols):
                    # if j == 0:  # 跳过第1列
                    #     continue
                    data_list.append(sheet_name.cell(i, j).value)
                model = Model()
                model.index = data_list[0]
                model.desc = data_list[1]
                model.url = data_list[2]
                model.method = data_list[3]
                model.headers = data_list[4]
                model.req_type = data_list[5]
                model.data = data_list[6]
                model.assert_data = data_list[7]
                model.assert_options = data_list[8]
                model.assert_value = data_list[9]
                model.extract = data_list[10]
                model.is_need = data_list[11]
                model.need_value = data_list[12]
                model.need_run = data_list[13]
                if model.need_run == 1:
                    models.append(model)
        return models
