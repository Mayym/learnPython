import time

# read是按字符读取文件的内容
# 允许输入参数决定读取几个字符，如果没有指定，从当前位置读取到结尾
# 否则，从当前位置读取指定个数字符

with open(r'test01.txt', 'r', encoding='utf-8') as f:
    strChar = f.read(1)  # 读一个位置就往后挪一个
    while strChar:
    # print(len(strChar))
        print(strChar, end='')
        strChar = f.read(1)
        time.sleep(0.5)


# 题目：
# 使用read读取文件，每次读取一个，使用循环读完
# 尽量保持格式