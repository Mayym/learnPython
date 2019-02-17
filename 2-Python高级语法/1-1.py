# lambda表达式

# 计算一个数字的100倍数
# 因为就是一个表达式，所以没有return
stm = lambda x: 100 * x
# 使用上跟函数调用一模一样
print(stm(2))

stm2 = lambda x,y,z: x + y*10 + z*100
print(stm2(1,2,3))
