# 三种方法的案例
class Person():
    # 实例方法
    def eat(self):
        print(self)
        print("Eating")

    # 类方法
    # 类方法的第一个参数，一般命名为cls，区别于self
    @classmethod
    def play(cls):
        print(cls)
        print("Playing")

    # 静态方法
    # 静态方法不需要第一个参数表示自身或者类
    @staticmethod
    def say():
        print("Saying")


may = Person()

# 实例方法
may.eat()
# 类方法
Person.play()
may.play()   # 能正常使用
# 静态方法
Person.say()
may.say()    # 能正常使用
