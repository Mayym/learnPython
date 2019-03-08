# collections模块
import collections

# namedtuple案例-1
# help(collections.namedtuple)
Point = collections.namedtuple("Point", ['x', 'y'])   # 相当于创建一个没有函数的类
p = Point(11, 22)

print(p.x)
print(p.y)
print(p[0])


# namedtuple案例-2
Circle = collections.namedtuple("Circle", ['x', 'y', 'r'])

c = Circle(100, 150, 50)
print(c)
print(type(c))
# 想检测以下namedtuple是属于谁的子类
print(isinstance(c, tuple))


# deque
from collections import deque

q = deque(['a', 'b', 'c'])
print(q)

q.append('d')
print(q)

q.appendleft('x')
print(q)
