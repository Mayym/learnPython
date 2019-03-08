# 闭包常见坑

def count():
    # 定义列表，列表里存放的是定义的函数
    fs = []
    for i in range(1,4):
        # 定义一个函数f
        # f是一个闭包结构，i是count的局部变量
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count()
print(f1())
print(f2())
print(f3())
# 期望返回1，4，9；但是结果是，9，9，9.
print('*' * 100)


# 修改上述函数
def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1,f2,f3 = count1()
print(f1())
print(f2())
print(f3())
