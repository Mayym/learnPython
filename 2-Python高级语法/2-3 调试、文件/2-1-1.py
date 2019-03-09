# with案例-2
with open(r'test01.txt', 'r', encoding='utf-8') as f:
    # 按行读取内容
    strline = f.readline()
    # 此结构保证能够完整读取文件直到结束
    while strline:
        print(strline.strip())
        strline = f.readline()
