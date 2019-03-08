# 排序案例

a = [234, 22312, 123, 45, 43, 2, 3, 66723, 34]
al = sorted(a, reverse=True)
print(al)


# 排序案例2

a = [-43, 23, 45, 6, -23, 2, -4345]
# 按照绝对值进行排序，按倒序排列
# abs是求绝对值的意思
al = sorted(a, key=abs, reverse=True)
print(al)


# sorted案例

astr = ['may', 'May', 'zym', 'Zym', 'Angela', 'Tom', 'zhengyimei']

str1 = sorted(astr)
print(str1)

str2 = sorted(astr, key=str.lower)
print(str2)
