# raise案例 -2
# 自己定义异常
# 需要注意：自定义异常必须是系统异常的子类

class MyError(ValueError):
    pass

try:
    print("May")
    print(3.1415926)
    # 手动引发一个异常
    # 注意语法: raise ErrorClassName
    raise MyError
    print("NO!")
except NameError as e:
    print("NameError:" + e)
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")
finally:
    print("执行这个代码")