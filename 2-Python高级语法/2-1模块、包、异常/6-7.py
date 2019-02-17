import shutil

# copy(): 复制文件
# 格式： shutil.copy(来源路径，目标路径)
# 返回值： 返回目标路径
# 拷贝的同时，可以给文件重命名
"""
rst = shutil.copy("C:\\Users\\15MR\MAY\learnPython\\2-Python高级语法\\6-6.py",
                  "C:\\Users\\15MR\MAY\learnPython\\2-Python高级语法\\6-6(1).py")
print(rst)
"""


# copy2(): 复制文件，保留元数据（文件信息：比如创建时间、所有者、权限等）
# 格式： shutil.copy2(来源路径，目标路径)
# 返回值： 返回目标路径
# 注意：copy和copy2的唯一区别在于copy2复制文件时尽量保留元数据


# copyfile(): 将一个文件中的内容复制到另外一个文件当中(会覆盖掉被拷贝文件的内容)
# 格式： shutil.copyfile('源路径', '目标路径')
# 返回值： 目标路径
"""
rst = shutil.copyfile("6-6.py", "1-2-1(1).py")
print(rst)
"""


# move(): 移动文件/文件夹
# 格式： shutil.move(源路径， 目标路径)
# 返回值： 目标路径
"""
rst = shutil.move("C:\\Users\\15MR\MAY\learnPython\\2-Python高级语法\\1-2-1(1).py", 
                  "C:\\Users\\15MR\MAY\learnPython\\2-Python高级语法\pkg01")
print(rst)
"""


# make_archive(): 归档操作
# 格式： shutil.make_archive('归档之后的目录和文件名'， '后缀'， '需要归档的文件夹')
# 返回值： 归档之后的地址
# help(shutil.make_archive)
# 是想得到一个叫may.zip的归档文件
"""
rst = shutil.make_archive("C:\\Users\\15MR\MAY\learnPython\\test", "zip", "C:\\Users\\15MR\MAY\learnPython\\test")
print(rst)   # 'C:\Users\15MR\MAY\learnPython\test.zip'
"""


# unpack_archive(): 解包操作
# 格式： shutil.unpack_archive('归档文件地址'. '解包之后的地址')
# 返回值： 解包之后的地址