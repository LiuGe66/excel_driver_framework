import os
from time import sleep

import pytest

pytest.main()
sleep(3)
os.system('allure generate ../temps -o ../report/report.html')
print('ffffffffffffffffffffffffffffffff')