# 1、调试

## 1.1调试技术
- 调试流程： 单元测试 -> 集成测试 -> 交测试部
- 分类
    - 静态调试：
    - 动态调试：

## 1.2pdb调试
- 推荐文章
    - [官方网页(英文)](https://docs.python.org/2/library/pdb.html)
    - [pdb模块介绍](https://blog.csdn.net/carolzhang8406/article/details/6923997)
        - 简单使用的介绍，推荐优先阅读
    - [pdb详细中文介绍](http://blog.csdn.net/wyb_009/article/details/8896744)
        - 主要是帮助文件的中文翻译
    - [调试案例01](https://www.cnblogs.com/dkblog/archive/2010/12/07/1980682.html)
    - [调试案例02](http://python.jobbole.com/81184/)
- pdb: python调试库

## 1.3pycharm调试
- run/debug模式
- 案例 1-3.py
- 断点： 程序的某一行，程序在debug模式下，遇到断点就会暂停
- Process finished with exit code 0
    - 0 表示程序正常执行
    - 1
    - -1
    
## 1.4单元测试
- 推荐文档
    - [官方测试文档集合](https://wiki.python.org/moin/PythonTestingToolsTaxonomy)
    - [测试案例01](http://blog.csdn.net/a542551042/article/details/46696635)
    - [PyUnit](https://wiki.python.org/moin/PyUnit)
    - [PyUnit详细讲解案例02](http://www.jb51.net/article/64119.htm)
    - [测试案例03](https://www.cnblogs.com/iamjqy/p/7155315.html)
 
    
# 2、文件

## 2.1 持久化-文件
- 文件
    - 长久保存信息的一种数据信息集合
    - 常用操作
        - 打开关闭（文件一旦打开，需要关闭操作）
        - 读写内容
        - 查找
- open函数
    - open函数负责打开文件，带有很多参数
    - 第一个参数： 必须有，文件的路径和名称
    - mode： 表明文件用什么方式打开
        - r： 以只读方式打开
        - w： 写方式打开，会覆盖以前的内容
        - x： 创建方式打开，如文件已经存在，报错
        - a： append方式，以追加的方式对文件内容进行写入
        - b： binary方式，二进制方式写入
        - t： 文本方式打开
        - +： 可读写
- 由于中文文档是‘gbk’的编码方式，我们需要将‘gbk’转化为utf-8，只要在打开文件的时候encode一下即可
    - open('file_name', 'r', encoding='utf-8')
- [案例 2-1.py]
- with语句
    - with语句使用的技术是一种成为上下文管理协议的技术（ContextManagementProtocol）
    - 自动判断文件的作用域，自动关闭不再使用的打开的文件句柄
- with open('file_name', 'r') as f:
    - f.readline() 按行读取     [案例 2-1-1.py]
    - l=list(f), for line in f:...  [案例 2-1-2.py]
    - f.read(n)  读取n个字符    [案例 2-1-3.py]
- seek（offset，from）   [案例 2-1-4.py]
    - 移动文件的读取位置，也叫读取指针
    - from的取值范围：
        - 0： 从文件头开始偏移
        - 1： 从文件当前位置开始偏移
        - 2： 从文件末尾开始偏移
    - 移动的单位是字节（byte）
    - 一个汉字由若干个字节构成
    - 返回文件只针对 当前位置
- 练习，[案例 2-1-5.py]

- tell函数： 用来显示文件读写指针的当前位置 [案例2-1-6.py]

## 2.2 文件的写操作-write
- write(str)： 把字符串写入文件
- writeline(str)： 把字符串按行写入单位
- 区别： [案例 2-2.py]
    - write函数参数只能是字符串
    - writeline参数可以是字符串，也可以是字符序列
    
## 2.3 持久化 -pickle
- 序列化（持久化，落地）： 把程序运行中的信息保存在磁盘上
- 反序列化： 序列化的逆过程
- pickle： python提供的序列化模块 [案例 2-3.py，2-3-1.py]
    - pickle.dump： 序列化
    - pickle.load： 反序列化
    
## 2.4 持久化 -shelve
- 持久化工具
- 类似字典，用kv对保存数据，存取方式跟字典也类似
- open，close
- [案例 2-4.py，2-4-1.py]
- shelve特性 [案例 2-4-2.py，2-4-3.py]
    - 不支持多个应用并行写入
        - 为了解决这个问题，open的时候可以使用flag=r
    - 写回问题 [案例 2-4-4.py，2-4-5.py]
        - shelve默认情况下不会等待持久化对象进行任何修改
        - 解决方法： 强制写回： writeback=True