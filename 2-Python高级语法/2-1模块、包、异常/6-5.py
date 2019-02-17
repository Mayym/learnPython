import os

"""os模块：方法部分"""
# getcwd(): 获取当前的工作目录
# 格式： os.getcwd()
# 返回值： 当前工作目录的字符串
# 当前工作目录就是程序在进行文件相关操作，默认查找文件的目录
mydir = os.getcwd()
print(mydir)


# chdir(): 改变当前的工作目录
# change directory
# 格式： os.chdir(路径)
# 返回值： 无
os.chdir("C:\\Users\\15MR\MAY\learnPython\\2-Python高级语法")
mydir = os.getcwd()
print(mydir)


# listdir(): 获取一个目录中所有子目录和文件的名称列表
# 格式： os.listdir(路径)
# 返回值： 所有子目录和文件名称的列表
print("*" * 100)
help(os.listdir)
print("*" * 100)

ld = os.listdir()
print(ld)
print("-" * 100)

# makedirs(): 递归创建文件夹
# 格式： os.makedirs(递归路径)
# 返回值： 无
# 递归路径： 多个文件夹层层包含的路径就是递归路径，如a\b\c...

# help(os.makedirs)
# rst = os.makedirs("May") # 在当前工作目录创建文件夹“May”
# print(rst)


# system(): 运行系统shell命令
# 格式： os.system(系统命令)
# 返回值： 打开一个shell或者终端界面
# ls(Linux),dir(Windows)是列出当前文件和文件夹的系统命令；0表示成功，1表示失败
# 一般推荐使用subprocess代替
rst = os.system("dir")
print(rst)

# 在当前目录下创建一个“May”的文件夹;Linux: touch May
# rst = os.system("md May")
# print(rst)


# getenv(): 获取指定的系统环境变量值
# 格式： os.getenv('环境变量名')
# 返回值： 指定环境变量名对应的值
rst = os.getenv("PATH")
print(rst)


# exit(): 退出当前程序
# 格式： exit()
# 返回值： 无


print("-" * 100)

"""os模块：值部分"""
# 写环境路径时不要手动拼写，使用os.path模块，可以在不同系统下执行，即可移植的
print(os.pardir)  # 父亲目录就是 ..
print(os.curdir)  # 当前目录就是 .
print(os.linesep) # 当前系统的换行符号
print(os.sep)     # 当前系统路径分隔符：Window下为反斜杠\；Linux下为斜杠/
print(os.name)    # linux操作系统的名称是posix
