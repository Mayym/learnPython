# 定义一个空的类
class Student():
    """定义一个学生类，用来形容学生"""
    # 一个空类，pass必须有
    pass


# 定义一个对象
Zym = Student()


# 定义一个类，用来描述试听Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 需要注意：def的缩进层级；系统默认有一个self参数
    def do_homework(self):
        print("%s在做作业"%self.name)
        # 推荐在函数末尾使用return语句
        return None


# 实例化一个叫May的学生，是一个具体的人
May = PythonStudent()
print(May.name)
print(May.age)
# 注意成员函数的调用没有传递参数
May.do_homework()