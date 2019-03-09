# tell函数案例
with open(r'test01.txt', 'r', encoding='utf-8') as f:
    pos = f.tell()
    print(pos)
    strChar = f.read(3)
    pos = f.tell()

    while strChar:
        print(strChar)
        print(pos)

        strChar = f.read(3)
        pos = f.tell()

# 结果表明：tell的返回数字的单位是byte
# read是以字符为单位