# 私有变量案例


class Person():
    # name是共有成员
    name = "May"
    # __age是私有成员
    __age = 18


p = Person()
# name是公有变量
print(p.name)
# __age是私有变量，print(p.__age)报错信息AttributeError: 'Person' object has no attribute '__age'

print("-" * 20)
# name mangling技术
print(Person.__dict__)
print(p._Person__age)

p._Person__age = 19
print(p._Person__age)
