import  logging

# logging.log(logging.INFO,"This is info ")
# logging.debug("This is debug")
logging.warning("设置的警告的提示信息")

# 第一步：
# 创建一个日志收集器：logging.getLogger("收集器的名字")

logger1 = logging.getLogger("我的第一个收集器")
#第二步：给日志收集器，设置日志级别：logger.setLevel(logging.INFO)
logger1.setLevel(logging.INFO)

#第三步：给日志收集器，创建一个输出渠道。handle1 = logging.StreamHandler()
handle1 =logging.StreamHandler()
#第四步：给渠道，设置一个日志输出内容的格式。
handle1.setLevel(logging.INFO)
fmt ='%(asctime)s %(name)s %(levelname)s %(filename)s-%(lineno)d line：%(message)s'
formatter = logging.Formatter(fmt)
handle1.setFormatter(formatter)

#第六步：将设置好的渠道，添加到日志收集器上。
logger1.addHandler(handle1)

logger1.info("test info")