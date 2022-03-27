# 1. 导包
import os
from time import sleep


# 2. 封装读取内存函数
def get_mem_data():
    # 调用os.popen()方法 -> 返回对象
    data = os.popen("adb shell dumpsys meminfo com.jabra.moments")
    # print(data)
    # 遍历
    for line in data:
        # print("------------")
        print(line)
        if "TOTAL" in line:
            # print(line.split())
            return line.split()[1]


if __name__ == '__main__':
    for i in range(10):
        mem = get_mem_data()
print("mem=", mem / 10)
sleep(1)
