import unittest, logging

from api.login_api import LoginApi
from utils import assert_common, read_login_data
from parameterized import parameterized


class TestIHRMLoginPa(unittest.TestCase):

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

    @parameterized.expand(read_login_data)
    def test_01_login(self,mobile, password, http_code, success, code, message):
        # 调用封装的登陆接口
        response = self.login_api.login(mobile, password)
        # 接收返回的json数据
        jsonData = response.json()
        # 调试输出登陆接口返回的数据
        logging.info("登陆成功时候输出的数据为：{}".format(jsonData))
        # 断言
        assert_common(self, http_code, response, success, code, message)
