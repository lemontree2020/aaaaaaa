import unittest, logging

import app
from api.login_api import LoginApi
from utils import assert_common


class Login(unittest.TestCase):

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

    def test_login(self):
        # 调用封装的登陆接口
        response = self.login_api.login("13800000002", "123456")
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登陆接口返回的数据
        logging.info("登陆成功时候输出的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, 200, response, True, 10000, "操作成功")

        # 获取令牌，并拼接成Bearer开头的
        token = jsonData.get("data")

        # 保存在全局变量app.py中
        app.HEADERS['Authorization'] = 'Bearer ' + token
        logging.info("保存的令牌是:{}".format(app.HEADERS))
