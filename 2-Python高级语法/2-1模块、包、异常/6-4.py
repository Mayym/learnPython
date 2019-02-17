import timeit

help(timeit.timeit)
print("*" * 100)


# timeit 可以执行一个函数，来测量一个函数的执行时间
def do_it():
    num = 3
    for i in range(num):
        print("Repeat for {0}".format(i))

# 执行函数，重复10次
t = timeit.timeit(stmt=do_it, number=10)
print(t)

print("-" * 100)



# 另一种写法
s = """
def do_it(num):
    for i in range(num):
        print("Repeat for {0}".format(i))
"""

# 执行do_it(num)，setup负责把环境变量准备好
# 实际相当于给timeit创造了一个小环境
# 在创作的小环境中，代码执行的顺序大致是：
'''
def do_it(num):
    ......
num = 3
do_it(num)
'''
    
t = timeit.timeit("do_it(num)", setup=s+"num=3", number=10)
print(t)
