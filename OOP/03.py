class Student():
    name = "May"
    age = 20

    def say(self):
        self.name = "zym"
        self.age = 22
        print("My name is {0}.".format(self.name))
        print("My age is {0}.".format(self.age))

    def say_again(s):
        print("My name is {0}.".format(s.name))
        print("My age is {0}.".format(s.age))


may = Student()
may.say()
may.say_again()
print("*" * 20)


class Teacher():
    name = "ym"
    age = 23

    def say(self):
        self.name = "may"
        self.age = 20
        print("My name is {0}.".format(self.name))
        print("My age is {0}.".format(self.age))
        # 调用类的成员变量需要用__class__
        print("My age is {0}.".format(__class__.age))

    def say_again():
        print(__class__.name)
        print(__class__.age)
        print("Hello, nice to see you again.")


t = Teacher()
t.say()
# t.say_again()报错，因为方法say_again()没有参数传入，但是该句会将实例t直接传入导致出错
# 调用绑定类函数时应使用类名
Teacher.say_again()
print("-" * 30)


# 关于self的案例


class A():
    name = "Tom"
    age = 18

    def __init__(self):
        self.name = "Max"
        self.age = 20

    def say(self):
        print(self.name)
        print(self.age)


class B():
    name = "Bob"
    age = 19


a = A()
# 此时，系统会默认把a作为第一个参数传入函数
a.say()
# A.say()会报错，因为A为类实例，系统无法默认将A作为参数传入__init__构造函数
# 此时，手动传入参数，self被a替换
A.say(a)
# 同样可以把A作为参数传入，此时打印的是类的属性
A.say(A)
# 此时，传入的是类实例B，因为B具有name和age属性，所以不会报错
A.say(B)

# 以上代码，利用了鸭子模型
