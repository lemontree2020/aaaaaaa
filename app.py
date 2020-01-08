# 编写初始化日志的函数
#

import logging
from logging import handlers
import os



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = "http://182.92.81.159"
HEADERS = {"Content-Type": "application/json"}
EMP_ID = ""


def init_logging():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 设置处理器
    # 设置控制台处理器
    sh = logging.StreamHandler()
    # 设置文件处理器
    # 获取当前文件所在位置
    filename = BASE_DIR + "/log/ihrm.log"
    # TimedRotatingFileHandler 可以按照时间切分日志
    fh = logging.handlers.TimedRotatingFileHandler(filename, when='M', interval=2, backupCount=5)
    # 实例化格式器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 将格式器添加给处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加给日志器
    logger.addHandler(sh)
    logger.addHandler(fh)
