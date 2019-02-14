# 组装类例子 -3
from types import MethodType

class A():
    pass

def say(self):
    print("Saying")


a = A()
a.say = MethodType(say, A)
a.say()

print(A.__dict__)
help(MethodType)


# 利用type造一个类
# 先定义类应该具有的成员函数
def say(self):
    print("Saying")

def talk(self):
    print("Talking")

# 用type来创建一个类
A = type("AName", (object, ), {"class_say": say, "class_talk": talk} )

# 然后可以像正常访问一样使用类
a = A()
print(A.__name__)
print(A.__dict__)
a.class_say()
a.class_talk()
