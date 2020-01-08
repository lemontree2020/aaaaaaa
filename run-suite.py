import unittest
import time

import app
from script.login import Login
from script.test_emp import TestIHRMEmp
from script.test_login import TestIHRMLogin
from tools.HTMLTestRunner import HTMLTestRunner

# 初始化测试条件

suite = unittest.TestSuite()
# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(Login))
suite.addTest(unittest.makeSuite(TestIHRMEmp))


# suite.addTest(unittest.makeSuite(TestIHRMLogin))

# 使用HTMLTestRunner执行测试套件，生成测试报告
# reporte_path = app.BASE_DIR + "/report/ihrm{}.html.".format(time.strftime("%Y%m%d %H%M%S"))
reporte_path = app.BASE_DIR + "/report/ihrm.html"



#  打开测试报告
with open(reporte_path, 'wb') as f:
    # 初始化HTMLTestRunner
    runner = HTMLTestRunner(f, verbosity=1, title="IHRM人力资源管理系统", description="V1.0.0")
    # 使用Runner运行测试套件
    runner.run(suite)
