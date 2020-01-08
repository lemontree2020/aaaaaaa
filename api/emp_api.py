import app
import requests


class EmpApi():

    def __init__(self):
        # 初始化添加员工的url

        self.emp_url = app.HOST + "/api/sys/user"
        # 初始化请求头
        # 注意：若要调用员工管理模块的相关接口时，需要先调用login.py接口
        # 获取到的app.HEADERS 才会是{"Content-Type":"application/json","Authorization":"Bearer xxxx-xxx-xxxx"}
        self.headers = app.HEADERS

    def add_emp(self, username, password):
        # 添加员工
        data = {
            "username": username,
            "mobile": password,
            "timeOfEntry": "2020-01-01",
            "formOfEmployment": 1,
            "workNumber": "1234",
            "departmentName": "测试",
            "departmentId": "1210411411066695680",
            "correctionTime": "2020-01-30T16:00:00.000Z"

        }

        # 发送添加员工请求
        response = requests.post(self.emp_url, json=data, headers=self.headers)
        # 返回添加员工接口的响应数据
        return response

    def query_emp(self):
        # 获取查询员工的url
        # 查询员工接口的url结构是：http://182.92.81.159/api/sys/user/xxxx，所以拼接时候要加上"/"
        url = self.emp_url + "/" + app.EMP_ID
        # 返回接口请求查询的结果,headers={"Conytent-Type":"application/json","Authorization":"Bearer nfd13135154664646"}
        return requests.get(url, headers=self.headers)

    def modify_emp(self, username):
        # 修改员工与查询员工的url一样
        url = self.emp_url + "/" + app.EMP_ID

        # 修改的数据为：
        data = {
            "username": username
        }
        # 返回修改员工数据
        return requests.put(url, json=data, headers=self.headers)

    def delete_emp(self):
        url = self.emp_url + "/" + app.EMP_ID
        return requests.delete(url,headers=self.headers)