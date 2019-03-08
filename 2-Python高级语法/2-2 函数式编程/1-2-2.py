# reduce

from functools import reduce

# 定义一个操作函数
# 加入操作函数只是相加
def my_add(x, y):
    return x + y

# 对于列表执行my_add的reduce操作
rst = reduce(my_add, [1,2,3,4,5,6])
print(rst)
