# 属性案例
# 创建Student类，描述学生类
# 学生具有Student.name属性，但name格式并不统一
class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.set_name(name)

    # 介绍下自己
    def intro(self):
        print("Hi, my name is {0}.".format(self.name))

    def set_name(self, name):
        self.name = name.upper()


s1 = Student("may", 23)
s2 = Student("tingTing", 26)

s1.intro()
s2.intro()
