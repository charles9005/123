# 1. 导包
import os
from time import sleep


# 2. 封装读取内存函数
def get_mem_data():
    # 调用os.popen()方法 -> 返回对象
    data = os.popen("adb shell dumpsys cpuinfo grep com.jabra.moments")
    print(data)
    # 遍历
    for line in data:
        # print("------------")
        print(line)
        if "com.jabra.moments" in line:
            # print(line.split())
            return line.split()[0]


if __name__ == '__main__':
    for i in range(10):
        mem = get_mem_data()
print("battery=", mem)
sleep(1)
