# 简单异常案例
try:
    num = int(input("Plz input your number:"))
    rst = 100 / num
    print("计算结果是： {0}".format(rst))
except:
    print("出错了")
    exit()    # exit是退出程序的意思
