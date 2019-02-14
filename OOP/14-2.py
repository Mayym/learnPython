# 组装类例子 -2
class A():
    pass

def say(self):
    print("Saying")


a = A()
a.say = say
a.say(a)
