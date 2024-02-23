import os
import json
import xlrd


class ExcelHandle(object):
    def __init__(self, sheet_name):
        # self.wb = openpyxl.load_workbook(filename=os.path.dirname(__file__)+'/excel_file/login_test_data.xlsx')
        # self.sn = self.wb.get_sheet_names
        self.wb = xlrd.open_workbook(filename=os.path.dirname(os.path.dirname(__file__)) + '/data/login_test_data.xlsx')
        self.sn = self.wb.sheet_by_name(sheet_name)

    def get_data(self):
        data = []
        data_key = self.sn.row_values(0)
        for i in range(1, self.sn.nrows):
            data_value = self.sn.row_values(i)
            unit_case = dict(zip(data_key, data_value))
            # 类型转换,excel单元格内文字为字符串类型
            for k in unit_case.keys():
                try:
                    unit_case[k] = json.loads(unit_case.get(k))
                except (json.decoder.JSONDecodeError, TypeError) as e:
                    continue
            data.append(unit_case)
        return data
