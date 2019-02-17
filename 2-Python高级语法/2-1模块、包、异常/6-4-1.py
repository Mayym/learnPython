# 测量程序运行时间间隔实验
import time


def p():
    time.sleep(3.6)


t1 = time.time()
p()
t2 = time.time()
print(t2 - t1)
