# 定义一个普通函数

def my_func(a):
    print("In my_func")
    return None

a = my_func(8)
print(a)


# 函数作为返回值返回，被返回的函数在函数体内定义

def my_func2():

    def my_func3():
        print("In my_func3")
        return 3
    return my_func3

# 使用上面定义
# 调用my_func2，返回一个函数my_func3，赋值给f3
f3 = my_func2()
print(type(f3))
print(f3)

f3()
print("-" * 100)
print(f3())


# 复杂一点的返回函数的例子
# args： 参数列表
# 1.my_func4定义函数，返回内部定义的函数my_func5
# 2.my_func5使用了外部变量，这个变量是my_func4的参数

def my_func4(*args):
    def my_func5():
        rst = 0
        for n in args:
            rst += n
        return rst
    return my_func5

f5 = my_func4(1,2,3,4,5,6,7,8,9,0)
# f5的调用方式
print(f5())

f6 = my_func4(10,20,30,40,50)
print(f6())