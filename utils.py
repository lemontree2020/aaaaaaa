# 封装断言
import json

import pymysql

import app


def assert_common(self, http_code, response, success, code, message):
    self.assertEqual(http_code, response.status_code)  # 响应状态码
    self.assertEqual(success, response.json().get("success"))  # 断言success
    self.assertEqual(code, response.json().get("code"))  # 断言code
    self.assertIn(message, response.json().get("message"))  # 断言meg


def read_login_data():
    # 定义读取登录数据方法
    data_path = app.BASE_DIR + "/data/login_data.json"
    # 文件路径
    # 打开文件
    with open(data_path, mode='r', encoding='utf-8') as f:
        # 加载文件为json格式
        jsonData = json.load(f)

        # 遍历文件取出数据并保存在列表中
        p_list = []
        for data in jsonData:
            mobile = data.get("mobile")
            password = data.get("password")
            http_code = data.get("http_code")
            success = data.get("success")
            code = data.get("code")
            message = data.get("message")
            p_list.append((mobile, password, http_code, success, code, message))
    print(p_list)
    return p_list


def read_add_emp_data():
    # 文件路径
    path = app.BASE_DIR + "/data/employee.json"
    # 打开文件
    with open(path, mode="r", encoding='utf-8') as f:
        # 加载文件中的json数据
        jsonData = json.load(f)
        add_emp_data = jsonData.get("add_emp")

        result_list = []

        username = add_emp_data.get("username")
        mobile = add_emp_data.get("mobile")
        http_code = add_emp_data.get("http_code")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        result_list.append((username, mobile, http_code, success, code, message))

    print("读取添加员工的数据为：", result_list)
    return result_list


def read_query_emp_data():
    # 文件路径
    path = app.BASE_DIR + "/data/employee.json"
    # 打开文件
    with open(path, mode="r", encoding='utf-8') as f:
        # 加载文件中的json数据
        jsonData = json.load(f)
        query_emp_data = jsonData.get("query_emp")

        query_list = []

        http_code = query_emp_data.get("http_code")
        success = query_emp_data.get("success")
        code = query_emp_data.get("code")
        message = query_emp_data.get("message")
        query_list.append((http_code, success, code, message))

        print("查询员工的数据为：", query_list)
        return query_list


def read_modify_emp_data():
    # 文件路径
    path = app.BASE_DIR + "/data/employee.json"
    # 打开文件
    with open(path, mode="r", encoding='utf-8') as f:
        # 加载文件中的json数据
        jsonData = json.load(f)
        modify_emp_data = jsonData.get("modify_emp")

        modify_list = []

        username = modify_emp_data.get("username")
        http_code = modify_emp_data.get("http_code")
        success = modify_emp_data.get("success")
        code = modify_emp_data.get("code")
        message = modify_emp_data.get("message")
        modify_list.append((username, http_code, success, code, message))

    print("修改员工的数据为：", modify_list)
    return modify_list


def read_delete_emp_data():
    # 文件路径
    path = app.BASE_DIR + "/data/employee.json"
    # 打开文件
    with open(path, mode="r", encoding='utf-8') as f:
        # 加载文件中的json数据
        jsonData = json.load(f)
        delete_emp_data = jsonData.get("delete_emp")

        delete_list = []

        http_code = delete_emp_data.get("http_code")
        success = delete_emp_data.get("success")
        code = delete_emp_data.get("code")
        message = delete_emp_data.get("message")
        delete_list.append((http_code, success, code, message))

    print("查询员工的数据为：", delete_list)
    return delete_list


class DBUtiles():
    def __init__(self, host='182.92.81.159', user='readuser', password='iHRM_user_2019', database='ihrm'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # __rnter__和__exit__是一对魔法方法，主要是和with结合使用
    # 如:with DBUtils as db
    # 我们就可以在with的代码块中使用db来执行sql语句，这个db就相当于self.cursor

    def __enter__(self):
        self.conn = pymysql.connect(self.host, self.user, self.password, self.database)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()

        if self.conn:
            self.cursor.close()


if __name__ == '__main__':
    read_modify_emp_data()
