from excel_reader.excel_reader import ExcelReader
from test_http_run.test_http_run import HttpRun


excel = ExcelReader()
hr = HttpRun()
models = ExcelReader().read()
hr.do_send_http(models=models)
