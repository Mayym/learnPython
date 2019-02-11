# 继承中的构造函数 -2


class Animal():
    pass


class BuruAni(Animal):
    def __init__(self, name):
        print("Buru Dongwu {0}".format(name))


class Dog(BuruAni):
    def __init__(self):
        print("I am a dog.")


class Cat(BuruAni):
    pass


d = Dog()
c = Cat("mini")     # 参数要相匹配

print(type(super))
help(super)
