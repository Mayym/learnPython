import os.path as op

# abspath(): 将路径转化为绝对路径
# 格式： os.path.abspath('路径')
# 返回值： 路径的绝对路径形式
# . 点号：代表当前目录； .. 双点： 代表父母路
absp = op.abspath(".")
print(absp)


# basename(): 获取路径中的文件名部分
# 格式： os.path.basename(路径)
# 返回值： 文件名字符串(最后一个文件夹名)
bn = op.basename("C:\\Users\\15MR\MAY\learnPython\\2-Python高级语法")
print(bn)

bn = op.basename("C:\\Users\\15MR\MAY\learnPython")
print(bn)


# join(): 将多个路径拼合成一个路径
# 格式： os.path.join(路径1，路径2)
# 返回值： 组合之后的新路径字符串
bd = "C:\\Users\\15MR\MAY\learnPython"
fn = "2-Python高级语法"

p = op.join(bd, fn)
print(p)


print("-" * 100)

# split(): 将路径切割为文件夹部分和当前文件部分
# 格式： os.path.split(路径)
# 返回值： 路径和文件名组成的元组
t = op.split("C:\\Users\\15MR\MAY\learnPython\\2-Python高级语法")
print(t)
d, p = t
print(d, p)


# isdir(): 检测是否是目录
# 格式： os.path.isdir(路径)
# 返回值： 布尔值
rst = op.isdir("C:\\Users\\15MR\\MAY\\learnPython\\2-Python高级语法\\6-6.py")
print(rst)
rst = op.isdir("C:\\Users\\15MR\\MAY\\learnPython\\2-Python高级语法")
print(rst)


print("-" * 100)

# exists(): 检测文件或者目录是否存在
# 格式： os.path.exists(路径)
# 返回值： 布尔值
e = op.exists("C:\\Users\\15MR")
print(e)
