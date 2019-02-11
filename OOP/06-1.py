# 构造函数的概念
# 继承中的构造函数 -1


class Animal():
    pass


class BuruAni(Animal):
    pass


class Dog(BuruAni):
    # __init__就是构造函数；每次实例化时第一个被调用；主要工作是进行初始化
    def __init__(self):
        print("I am a dog.")


# 实例化的时候，括号内的参数需要跟构造函数参数匹配
# 实例化的时候，自动调用了Dog的构造函数
mini = Dog()
