# 组装一个类 -1
class A():
    pass

def say(self):
    print("Saying")

say(9)
print("-" * 60)

# 函数名可以当变量使用
A.say = say
a = A()
a.say()
print("-" * 60)

# 函数名可以当变量使用
sayagain = say
sayagain(9)
