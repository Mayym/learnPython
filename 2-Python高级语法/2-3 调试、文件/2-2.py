# write案例
# 1. 向文件追加一句诗

# a代表追加方式打开
with open(r'test01.txt', 'a', encoding='utf-8') as f:
    # 注意字符串内含有换行符
    f.write("\n\n生活不仅有眼前的苟且，\n还有诗和远方。\n")
    # 可以直接写入行，用writelines：表示写入很多行，参数可以是list格式
    l = ['天才在左','疯子在右']
    f.writelines(l)