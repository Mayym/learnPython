# 关于读取文件的练习
# 打开文件，三个字符一组读取内容，然后显示在屏幕上
# 每读一次，休息1秒钟（让程序暂停，可以使用time下的sleep函数）

import time

with open(r'test01.txt', 'r', encoding='utf-8') as f:
    # read参数的单位是字符，可以理解成一个汉字就是一个字符
    strChar = f.read(3)
    while strChar:
        print(strChar, end='')
        # sleep参数单位是秒
        time.sleep(1)
        strChar = f.read(3)