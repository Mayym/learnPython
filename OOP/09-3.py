# property
class A():
    def __init__(self):
        self.name = "may"
        self.age = 22

    # 此功能，是对类变量进行读取操作的时候应该执行的函数功能
    def fget(self):
        print("读取")
        return self.name

    # 模拟的是对变量进行写操作的时候执行的功能
    def fset(self, name):
        print("写入")
        self.name = "名字:" + name

    # fdel模拟的是删除变量时进行的操作
    def fdel(self):
        pass

    # property的四个参数顺序是固定
    name2 = property(fget, fset, fdel, "这是一个property的例子")


a = A()
print(a.name)
print(a.name2)

a.name2 = "zym"
print(a.name2)
