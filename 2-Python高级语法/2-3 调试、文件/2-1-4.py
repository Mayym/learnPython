# seek案例
# 打开文件后，从第5个字节处开始读取

# 打开读写指针在0处，即文件的开头
with open(r'test01.txt', 'r', encoding='utf-8') as f:
    # seek移动单位是字节，测试可知一个中文字符占用3个字节
    f.seek(6, 0)
    strChar = f.read()
    print(strChar)

