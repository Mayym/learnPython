# 多继承的例子
# 子类可以直接拥有父类的属性和方法，私有属性和方法除外


class Fish():
    def __init__(self, name):
        self.name = name

    def swim(self):
        print("I am swimming.")


class Bird():
    def __init__(self, name):
        self.name = nmae

    def fly(self):
        print("I am flying.")


class Person():
    def __init__(self, name):
        self.name = name

    def work(self):
        print("I am working.")


class SuperMan(Person, Bird, Fish):
    def __init__(self, name):
        self.name = name


s = SuperMan("may")
s.fly()
s.swim()

# 单继承的例子


class Student(Person):
    def __init__(self, name):
        self.name = name


t = Student("May")
t.work()
