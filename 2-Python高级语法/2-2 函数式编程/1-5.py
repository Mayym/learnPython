# 装饰器

def hello():
    print("Hello, world!")

hello()

f = hello
f()

# f和hello是一个函数
print(id(f))
print(id(hello))
print(f.__name__)
print(hello.__name__)

print('-' * 100)

# 现在有新的需求：对hello功能进行扩展，每次打印hello之前打印当前系统时间
# 而实现这个功能又不能改变现有代码
# -->使用装饰器来完成

import time
# 高阶函数，以函数作为参数
def print_time(f):
    def wrapper(*args, **kwargs):
        print("Time: ", time.ctime())
        return f(*args, **kwargs)
    return wrapper

# 上面定义了装饰器，使用的时候需要用到@，此符号是python的语法糖
@print_time
def hello():
    print("Hello, world!")

hello()

print("-" * 100)

# 装饰器的好处是，一旦定义，则可以装饰任意函数
def hello2():
    print("Hello, May!")
    print("Hi!")

hello2()

print("-" * 100)

@print_time
def hello2():
    print("Hello, May!")
    print("Hi!")

hello2()

print("-" * 100)

# 手动执行装饰器
def hello3():
    print("Hello, zym!")

hello3()


hello3 = print_time(hello3)
hello3()

print("-" * 100)
# 以下执行了两次打印时间
f = print_time(hello3)
f()