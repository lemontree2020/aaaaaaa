import requests
import app


class LoginApi():

    def __init__(self):
        self.login_url = app.HOST + "/api/sys/login"
        self.headers = app.HEADERS

    def login(self, mobile, password):
        # 使用data接收外部文件传入的mobile和password，拼接成要发送请求的数据
        data = {
            "mobile": mobile,
            "password": password
        }
        # 发送接口请求
        response = requests.post(self.login_url,
                                 json=data,
                                 headers=self.headers)

        # 返回响应数据
        return response
