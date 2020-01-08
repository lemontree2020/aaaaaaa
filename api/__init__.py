import app
import logging

# 初始化日志
app.init_logging()


#为什么要在api.__init__.py中初始化日志呢？
# 因为我们后面进行接口测试时，会调用封装的API接口，调用时会自动运行init函数，初始化日志器，从而实现自动初始化日志的功能
logging.info("test日志器能不能正常工作")