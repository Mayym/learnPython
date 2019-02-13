# 继承的语法
# 在python中，任何类都有一个共同的父类叫object

# 该空括号可以省略，但建议写上
class Person():
    name = "NoName"
    age = 18
    __score = 0           # 成绩，是秘密，只要自己知道
    _petname = "sec"    # 小名，是保护的，子类可以用，但不能公用

    def sleep(self):
        print("Sleeping...")

    def work(self):
        print("make some money")


# 父类写在括号里
class Teacher(Person):
    teacher_id = "9527"
    name = "May"

    def make_test(self):
        print("attention")

    def work(self):
        # 扩充父类的功能只需要调用父类相应的函数
        # 方法一：Person.work(self)
        # 方法二：super代表得到父类
        super().work()  # super(Teacher, self).work()
        self.make_test()


print(Teacher.name)

t = Teacher()
print(t.name)
print(t.age)
print(t._petname)
# t.__age公开访问私有变量，报错

t.sleep()
print(t.teacher_id)
print(t.name)
t.make_test()
t.work()
