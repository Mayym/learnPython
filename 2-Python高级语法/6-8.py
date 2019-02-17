import zipfile

# zipfile.ZipFile(file[, mode[, compression[, allowZip64] ]])
# 创建一个ZipFile对象，表示一个zip文件。参数file表示文件的路径或类文件对象(file-like object)
zf = zipfile.ZipFile("C:\\Users\\15MR\MAY\learnPython\\test.zip", 'r')


# ZipFile.getinfo(name): 获取zip文档内指定文件的信息。返回一个zipfile.ZipInfo对象，它包括文件的详细信息。
rst = zf.getinfo('test/1.txt')
print(rst)


# ZipFile.namelist(): 获取zip文档内所有文件的名称列表
nl = zf.namelist()
print(nl)
for f_name in nl:
    print(f_name)


# ZipFile.extractall([path[, members[, pwd]]]): 解压zip文档中的所有文件到当前目录。
"""
rst = zf.extractall("C:\\Users\\15MR\MAY\learnPython")
print(rst)
"""