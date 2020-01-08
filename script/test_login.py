import unittest, logging

from api.login_api import LoginApi
from utils import assert_common


class TestIHRMLogin(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        # 实例化对象
        cls.login_api = LoginApi()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_01_login_success(self):
        # 调用封装的登陆接口
        response = self.login_api.login("13800000002", "123456")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登陆接口返回的数据
        logging.info("登陆成功时候输出的数据为：{}".format(jsonData))
        # 断言
        # self.assertEqual(200, response.status_code)  # 响应状态码
        # self.assertEqual(True, jsonData.get("success"))  # 断言success
        # self.assertEqual(10000, jsonData.get("code"))  # 断言code
        # self.assertIn("操作成功", jsonData.get("message"))  # 断言meg

        # 调用utils断言
        assert_common(self, 200, response, True, 10000, "操作成功")

    def test_02_username_is_not_exist(self):
        # 调用封装的登陆接口
        response = self.login_api.login("139000000002", "123456")
        # 接收返回响应的json数据
        jsonData = response.json()
        # 调试输出的登陆接口返回的数据
        logging.info("账号不存在时候输出结果为：{}".format(jsonData))
        # 断言
        assert_common(self, 200, response, False, 20001, "用户名或密码错误")

    def test_03_password_error(self):
        # 调用封装的登陆接口
        response = self.login_api.login("138000000002", "error")
        # 接收返回响应的json数据
        jsonData = response.json()
        # 输出
        logging.info("密码错误时候的输出数据为：{}".format(jsonData))
        # 断言
        assert_common(self, 200, response, False, 20001, "密码错误")


    def test_04_username_has_special_var(self):
        # 调用封装的登陆接口
        response = self.login_api.login("13!@#$%%002", "error")
        # 接收返回响应的json数据
        jsonData = response.json()
        # 输出
        logging.info("用户名有特殊字符时候的输出数据为：{}".format(jsonData))
        # 断言
        assert_common(self, 200, response, False, 20001, "密码错误")

    def test_05_password_is_empty(self):
        # 调用封装的登陆接口
        response = self.login_api.login("138000000002","")
        # 接收返回响应的json数据
        jsonData = response.json()
        # 输出
        logging.info("密码为空时候的输出数据为：{}".format(jsonData))
        # 断言
        assert_common(self, 200, response, False, 20001, "密码错误")


    def test_06_username_has_chinese(self):
        # 调用封装的登陆接口
        response = self.login_api.login("138中国哈0002","123456")
        # 接收返回响应的json数据
        jsonData = response.json()
        # 输出
        logging.info("用户名有中文时候的输出数据为：{}".format(jsonData))
        # 断言
        assert_common(self, 200, response, False, 20001, "密码错误")

    def test_07_username_is_empty(self):
        # 调用封装的登陆接口
        response = self.login_api.login("","123456")
        # 接收返回响应的json数据
        jsonData = response.json()
        # 输出
        logging.info("用户名为空时候的输出数据为：{}".format(jsonData))
        # 断言
        assert_common(self, 200, response, False, 20001, "密码错误")

    def test_08_username_has_space(self):
        # 调用封装的登陆接口
        response = self.login_api.login("182000000 2","123456")
        # 接收返回响应的json数据
        jsonData = response.json()
        # 输出
        logging.info("用户名有空格时候的输出数据为：{}".format(jsonData))
        # 断言
        assert_common(self, 200, response, False, 20001, "密码错误")
