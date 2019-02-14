# 包含一个学生类
# 一个say_hello函数
# 一个打印语句


class Student():
    def __init__(self, name="NoNae", age=18):
        self.name = name
        self.age = age

    def say(self):
        print("My name is {0}".format(self.name))


def say_hello():
    print("Hello!")


# 当文件自己运行，执行print
# 当文件作为模块导入，则不执行
if __name__ == '__main__':
    print("I am module m01.")
