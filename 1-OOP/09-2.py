# property案例
# 定义一个Person类，具有name，age属性
# 对于任意输入的姓名，我们希望都用大写方式保存；年龄统一用整数保存

class Person():
    # 函数的名称可以任意
    def fget(self):
        return self._name * 2

    def fset(self, name):
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget, fset, fdel, "对name进行操作")

p1 = Person()
p1.name = "may"
print(p1.name)
