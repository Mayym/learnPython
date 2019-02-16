# raise案例 -1
try:
    print("May")
    print(3.1415926)
    # 手动引发一个异常
    # 注意语法: raise ErrorClassName
    raise ValueError
    print("NO!")
except NameError as e:
    print("NameError:" + e)
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")
finally:
    print("执行这个代码")