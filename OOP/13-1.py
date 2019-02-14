# 抽象
class Animal():
    def say_hello(self):
        pass


class Dog(Animal):
    def say_hello(self):
        super().say_hello()
        print("闻闻味道")


class Person(Animal):
    def say_hello(self):
        super().say_hello()
        print("招手")


d = Dog()
d.say_hello()

p = Person()
p.say_hello()
