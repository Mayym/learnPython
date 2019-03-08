# map举例

# 有一个列表，想对列表里的每一个元素乘以10，并得到新的列表
l1 = [i for i in range(10)]
print(l1)

l2 = []
for i in l1:
    l2.append(i * 10)

print(l2)

print("-" * 100)


# 利用map实现
def mul_ten(n):
    return n * 10

l3 = map(mul_ten, l1)
# print(list(l3))   (一)
# map类型是一个可迭代的结构，所以可以使用for遍历
'''
for i in l3:
    print(i)        （二）
'''



l4 = [i for i in l3]    # （三）
print(l4)

# （一）、（二）、（三）不管哪句先运行，剩下在运行其他语句得到的结果都为空，为什么？
