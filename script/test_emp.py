import logging
import unittest
import pymysql
from utils import DBUtiles
import app
from api.emp_api import EmpApi
from utils import assert_common, read_add_emp_data, read_query_emp_data, read_modify_emp_data, read_delete_emp_data
from parameterized import parameterized


class TestIHRMEmp(unittest.TestCase):

    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        # 实例化对象
        cls.emp_api = EmpApi()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @parameterized.expand(read_add_emp_data)
    def test_01_add_emp(self, username, mobile, http_code, success, code, message):
        # 调用员工添加接口
        response = self.emp_api.add_emp(username, mobile)
        # 获取添加员工接口的json数据
        jsonData = response.json()
        # 输出json数据
        logging.info("添加员工返回的数据为：{}".format(jsonData))
        # 获取员工ID并保存在全局变量中
        app.EMP_ID = jsonData.get("data").get("id")
        logging.info("员工ID：{}".format(app.EMP_ID))
        # 断言
        assert_common(self, http_code, response, success, code, message)

    @parameterized.expand(read_query_emp_data)
    def test_02_query_emp(self, http_code, success, code, message):
        # 调用查询员工接口
        response = self.emp_api.query_emp()
        # 获取json数据
        jsonData = response.json()
        # 输出
        logging.info("查询员工返回的数据为；{}".format(jsonData))
        # 断言
        assert_common(self, http_code, response, success, code, message)

    @parameterized.expand(read_modify_emp_data)
    def test_03_modify_emp(self, username, http_code, success, code, message):
        # 调用查询员工接口
        response = self.emp_api.modify_emp(username)
        # 获取json数据
        jsonData = response.json()
        # 输出json数据
        logging.info("修改员工返回的数据为；{}".format(jsonData))

        with DBUtiles() as db_utils:
            # 执行查询语句，查询出添加的员工的username是不是修改的username
            sql = "select username from bs_user where id ={}".format(app.EMP_ID)
            db_utils.execute(sql)
            # 获取执行结果
            result = db_utils.fetchone()[0]
            # 打印
            logging.info("在数据库中的username为：{}".format(db_utils.fetchone()))

        # 断言
        assert_common(self, http_code, response, success, code, message)

    @parameterized.expand(read_delete_emp_data)
    def test_04_delete_emp(self, http_code, success, code, message):
        # 调用删除员工接口
        response = self.emp_api.delete_emp()
        # 获取json数据
        jsonData = response.json()
        # 输出
        logging.info("删除员工返回的数据为；{}".format(jsonData))
        # 断言
        assert_common(self, http_code, response, success, code, message)
