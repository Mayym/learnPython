# 简单异常案例，给出提示信息
try:
    num = int(input("Plz input your number:"))
    rst = 100 / num
    print("计算结果是： {0}".format(rst))

# 如果是多种error的情况，需要把越具体的错误越往前放
# 在异常类继承关系中，越是子类的异常，越要往前方
# 越是父类的异常，越要往后放

# 在处理异常的时候，一旦拦截到某一个异常，则不再继续往下查看，直接进行下一个代码
# 即有finally则执行finally语句块，否则就执行下一个大的语句
except ZeroDivisionError as e:
    print(e)
    print("请不要输入数字0")
    exit()
except NameError as e:
    print(e)
    print("名字错误")
    exit()
except AttributeError as e:
    print(e)
    print("属性有问题")
    exit()
except ValueError as e:
    print(e)
    print("值的类型错了")
# 所有异常都是继承自Exception
# 如果写上下面这句话，任何异常都会拦截住
except Exception as e:
    print(e)
    print("不知道什么原因出错了")
