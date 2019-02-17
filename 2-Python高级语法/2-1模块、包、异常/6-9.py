import random

# random(): 获取0-1之间的随机小数
# 格式： random.random()
# 返回值： 随机0-1之间的小数
print(random.random())

# 随机生成0-100之间的整数
print(int(random.random() * 100))


# choice(): 随机返回序列中的某个值
# 格式： random.choice(序列)
# 返回值： 序列中的某个值
l = [str(i)+"haha" for i in range(10)]
print(l)
rst = random.choice(l)
print(rst)


# shuffle(): 随机打乱列表（原地打乱）
# 格式： random.shuffle(列表)
# 返回值： 无
l1 = [i for i in range(10)]
print(l1)
l2 = random.shuffle(l1)
print(l2)
print(l1)


# random.randint():
# 随机生成0-100的整数（包含0和100）
print(random.randint(0, 100))
