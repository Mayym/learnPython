# 1、模块
- 一个模块就是一个包含python代码的文件，后缀名是.py，就是个python文件。
- 使用模块的原因
    - 程序太大，编写维护不方便，需要拆分
    - 模块可以增加代码重复利用的方式
    - 当做命名空间使用，避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件，所以任何代码可以直接书写
    - 不过根据模块的规范，最好在模块中编写以下内容：
        - 函数 （单一功能）
        - 类 （相似功能的组合，或者类似业务模块）
        -测试代码
- 如何使用模块
    - 模块直接导入 （模块m01.py）
        - 假如模块名称直接以数字开头时，需要借助importlib包实现导入
        - importlib语法
            
              import importlib
              module = importlib.import_module("01")  
              # 相当于导入了一个叫01的模块并把导入模块赋值给module
              m = module.function_name()
    
    - 直接导入语法 （f01.py）
    
             import module_name
             module_name.function_name
             module_name.class_name
            
    - import 模块 as 别名 （f02.py）
        - 导入的同时给模块起一个别名
        - 其余用法相同
    
    - from module_name import func_name, class_name (f03.py)
        - 按上述方法有选择性的导入
        - 使用的时候可以直接使用导入的内容，不需要前缀
        
    -from module_name import *
        - 导入模块所有内容
        - f04.py
    
- if __name__ == '__main__'的使用
    - 可以有效避免模块代码被导入的时候被动执行的问题
    - 建议所有程序的入口都以此代码为入口

# 2、模块的搜索路径和存储
- 模块的搜索路径
    - 加载模块的时候，系统会在那些地方寻找此模块
- 系统默认的模块搜索路径（f05.py）
    
        import sys
        sys.path 属性可以获取路径列表
- 添加搜索路径

        sys.path.append(dir)
- 模块的加载顺序
    1. 搜索内容中已经加载好的模块
    2. 搜索python的内置模块
    3. 搜索sys.path路径
    
# 3、包
- 包是一种组织管理代码的方式，包里面存放的是模块
- 用于将模块包含在一起的文件夹就是包
- 自定义包的结构

        |---包
        |---|--- __init__.py  包的标志文件
        |---|--- 模块1
        |---|--- 模块2
        |---|--- 子包（子文件夹）
        |---|---|--- __init__.py
        |---|---|--- 子包模块1
        |---|---|--- 子包模块2
        
- 包的导入操作
    - import package_name
        - 直接导入一个包，可以使用__init__.py中的内容
        - 使用方式：
        
                package_name.func_name
                package_name.class_name.func_name()
        - 此种方式的访问内容是
        - 案例 pkg01, f06.py
    - import package_name as p
        - 具体用法跟作用方式，跟上述简单导入一致
        - 注意的是此种方法是默认对__init__.py内容的导入
    - import package.module
        - 导入包中某一个具体的模块
        - 使用方法
        
                package.module.func_name
                package.module.class.func_name
                package.module.class.var
        - 案例 f07.py
    - import package.module as pm

- from ... import 导入
    - from package import module1, module2, module3, ...
        - 此种导入方法不执行'__init__'的内容
    
                from pkg01 import p01
                p01.say_hello()
    - from package import *
        - 导入当前包'__init__.py'文件中所有的函数和类
        - 使用方法
                
                func_name()
                class_name.func_name()
                class_name.var
        - 案例 f08.py， 注意此种导入的具体内容
    
- from package.module import *
    - 导入包中指定模块的所有内容
    - 使用方法
    
        func_name()
        class_name.func_name()
        
- 在开发环境中经常会引用其他模块，可以在当前包中直接导入其他模块中的内容
    - import 完整的包或者模块的路径
    
- '__all__'的用法
    - 在使用from package import * 的时候，* 可以导入的内容
    - '__init__.py'中如果文件为空，或者没有'__all__'，那么只可以把'__init__'中的内容导入
    - '__init__'如果设置了'__all__'的值，那么则按照'__all__'指定的子包或者模块进行导入，
        如此则不会载入'__init__'中的内容
    
            '__all__' = ['module1', 'module2', 'package1', ...]
    - 案例 f09.py
    
# 4、命名空间
- 用于区分不同位置不同功能但相同名称的函数或者变量的一个特定前缀
- 作用是防止命名冲突

        set_name()
        Student.set_name()
        Dog.set_name()
        
# 5、异常
- 广义上的错误分为错误和异常
    - 错误：指的是可以人为避免
    - 异常：指在语法逻辑正确的前提下，出现的问题
- 在python里，异常是一个类，可以处理和使用
- 异常的分类

        AssertError  断言语句（assert）失败
        AttributeError  尝试访问未知的对象属性
        EOFError  用户输入文件末尾标志EOF（Ctrl+d）
        FloatingPointError  点数计算错误
        GeneratorExit  generator.close()方法被调用的时候
        ImportError  导入模块失败的时候
        IndexError  索引超出序列的范围
        KeyError  字典中查找一个不存在的关键字
        KeyboardInterrupt  用户输入中断键（Ctrl+c）
        MemoryError  内存溢出（可通过删除对象释放内存）
        NameError  尝试访问一个不存在的变量
        NotImplementedError  尚未实现的方法
        OSError  操作系统产生的异常（例如打开一个不存在的文件）
        OverflowError  数值运算超出最大限制
        ReferenceError  弱引用（weak reference）试图访问一个已经被垃圾回收机制回收了的对象
        RuntimeError  一般的运行时错误
        StopIteration  迭代器没有更多的值
        SyntaxError  Python的语法错误
        IndentationError  缩进错误
        TabError  Tab和空格混合使用
        SystemError  Python的编译器系统错误
        SystemExit  Python编译器进程被关闭
        TypeError  不同类型间的无效操作
        UnboundLocalError  访问一个未初始化的本地变量（NameError的子类）
        UnicodeError  Unicode相关的错误（ValueError的子类）
        UnicodeEncodeError  Unicode编码时的错误（UnicodeError的子类）
        UnicodeDecodeError  Unicode解码时的错误（UnicodeError的子类）
        UnicodeTranslateError  Unicode转换时的错误（UnicodeError的子类）
        ValueError  传入无效的参数
        ZeroDivisionError  除数为零

- 异常处理
    - 不能保证程序永远正确运行
    - 但是，必须保证程序在最坏的情况下得到的问题被妥善处理
    - python的异常处理模块全部语法为：
    
            try:
                尝试实现某个操作，
                如果没出现异常，任务就可以完成
                如果出现异常，将异常从当前代码块扔出去尝试解决异常
            
            except 异常类型1：
                解决方案1：用于尝试在此处处理异常解决问题
            
            except 异常类型2：
                解决方案2：用于尝试在此处处理异常解决问题
            
            except(异常类型1，异常类型2...)
                解决方案：针对多个异常使用相同的处理方式
            
            except:
                解决方案：所有异常的解决方案
                
            else:
                如果没有出现任何异常，将会执行此处代码
                
            finally:
                不管有无异常都要执行的代码
                
    - 流程
        1. 执行try下面的语句
        2. 如果出现异常，则在except语句里查找对应异常并进行处理
        3. 如果没有出现异常，则执行else语句内容
        4. 最后，不管是否出现异常，都要执行finally语句
    - 除except（至少一个）以外，else和finally可以没有
    - 案例 5-1.py，5-2.py

- 用户手动引发异常
    - 当某些情况，用户希望自己引发一个异常的时候，可以使用
    - raise关键字来引发异常（案例 5-3.py，5-4.py）
- else语句案例（案例 5-5.py）
- 关于自定义异常
    - 只要是raise异常，则推荐自定义异常
    - 在自定义异常的时候，一般包含以下内容：
        - 自定义发生异常的异常代码
        - 自定义发生异常后的问题提示
        - 自定义发生异常的行数
- 最终的目的是，一旦发生异常，方便程序员快速定位错误现场

# 6、常用模块
- calendar
- time
- datetime
- timeit
- os
- shutil
- zip
- math
- string
- 上述所有模块使用理论上都应该先导入，string是特例
- calendar，time，datetime的区别参考中文意思

## 6.1 calendar模块
- 案例 6-1.py
- 跟日历相关的模块
    - calendar.calendar(year): 获取一年的日历字符串
    - calendar.isleap(year): 判断某一年是否闰年
    - calendar.leapdays(y1, y2): 获取指定年份之间的闰年的个数
    - calendar.month(year, month): 获取某个月的日历字符串
    - calendar.monthrange(year, month): 获取一个月的周几开始即和天数
        - 回值： 元组（周几开始，总天数）
        - 注意： 周默认0-6表示周一到周天
    - calendar.monthcalendar(year, month): 返回一个月每天的矩阵列表
        - 回值： 二级列表
        - 注意： 矩阵中没有天数用0表示
    - calendar.prcal(year): 直接打印日历
    - calendar.prmonth(year, month): 直接打印整个月的日历
    - calendar.weekday(year, month, day): 获取周几
    
## 6.2 time模块
- 案例 6-2.py
- 时间戳
    - 一个时间表示，根据不同语言，可以是整数或者浮点数
    - 是从1970年1月1日0时0分0秒到现在经历的秒数
    - 如果表示的时间是1970年以前或者太遥远的未来，可能出现异常
    - 32位操作系统能够支持到2038年
- UTC时间
    - UTC又称世界协调时间，以英国的格林尼治天文所在的地区的时间为参考时间，也叫做世界标准时间
    - 中国时间是 UTC+8 东八区
- 夏令时
    - 夏令时就是夏天的时候将时间调快一个小时，本意是督促大家早睡早起节省蜡烛。
        每天变成25个小时，本质没变还是24小时
- 时间元组
    - 一个包含时间内容的普通元组
    
            索引  内容       属性       值
            
            0     年       tm_year    2015
            1     月       tm_mon     1~12
            2     日       tm_mday    1~31
            3     时       tm_hour    0~23
            4     分       tm_min     0~59
            5     秒       tm_sec     0~61 60表示闰秒，61保留值
            6     周几     tm_wday    0~6
            7     第几天   tm_yday    1~366
            8     夏令时   tm_isdst   0,1,-1(表示夏令时)
            
- 需要单独导入 import time
    - time.timezone: 当前时区和UTC时间相差的秒数，在没有夏令时的情况下的间隔，东八区的是-28800
    - time.altzone: 获取当前时区与UTC时间相差的秒数，在有夏令时的情况下，东八区的是-32400
    - time.daylight: 测试当前是否是夏令时时间的状态，0 表示是
    - time.time(): 得到时间戳
    - time.localtime(): 得到当前时间的时间元组；可以通过点号操作符得到相应的属性元素的内容
    - time.asctime(时间元组): 返回元组的正常字符串化之后的时间格式
    - time.ctime(): 获取字符串化的当前时间
    - time.mktime(时间元组): 使用时间元组获取对应的时间戳
    - time.clock(): 获取cpu时间， 3.0-3.3版本直接使用
        - 案例 6-2-1.py
        - python3.8后使用： time.perf_counter()
        - DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: 
            use time.perf_counter or time.process_time instead time.clock()
    - time.sleep(secs): 使程序进入睡眠，n秒后继续
    - time.strftime(): 将时间元组转化为自定义的字符串格式（案例 6-2-2.py）
        
    
            格式     含义                                          备注
             %a   本地(locale)简化星期名称
             %A   本地完整星期名称
             %b   本地简化月份名称
             %B   本地完整月份名称
             %c   本地相应的日期和时间表示
             %d   一个月中的第几天(01-31)
             %H   一天中的第几个小时(24小时制，00-23)
             %I   一天中的第几个小时(12小时制，01-12)
             %j   一年中的第几天(001-366)
             %m   月份(01-12)
             %M   分钟数(00-59)
             %p   本地 am 或者 pm 的相应符                          注1
             %S   秒(01-61)                                       注2
             %U   一年中的星期数(00-53 星期天是一个星期的开始) 
                    第一个星期天之前的所有天数都放在第0周             注3
             %w   一个星期中的第几天(0-6, 0是星期天)                 注3
             %W   和 %U 基本相同，不同的是 %W 以星期一为一个星期的开始
             %x   本地相应日期
             %X   本地相应时间
             %y   去掉世纪的年份(00-99)
             %Y   完整的年份
             %z   用 +HHMM 或 -HHMM 表示距离格林威治的时区偏移
                    (H 代表十进制的小时数，M 代表十进制的分钟数)
             %%   %号本身
             
## 6.3 datetime模块
- 案例 6-3.py
- datetime提供日期和时间的运算和表示
- datetime常见属性
    - datetime.date: 一个理想和的日期，提供year, month, day属性
    - datetime.time: 提供一个理想和的时间，具有hour, minute, sec, microsec等内容
    - datetime.datetime: 提供日期跟时间的组合
        - from datetime import datetime 该语句后可直接使用datetime
        - 常用类方法：
            - today
            - now
            - utcnow
            - fromtimestamp: 从时间戳返回本地时间
    - datetime.timedelta: 提供一个时间差，时间长度
    
## 6.4 timeit模块
- timeit-时间测量工具
- 案例 6-4.py
    - 6-4-1.py： 测量程序运行时间间隔实验
    - 6-4-2.py： 生成列表两种方法的比较