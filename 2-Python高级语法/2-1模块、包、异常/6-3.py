import datetime
import time

# datetime.date: 一个理想和的日期，提供year, month, day属性
dt = datetime.date(2019, 2, 16)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print("-" * 100)


# datetime.time: 提供一个理想和的时间，具有hour, minute, sec, microsec等内容
dt = datetime.time(15, 15, 47, 551709)
print(dt)
print("-" * 100)


# datetime.datetime: 提供日期跟时间的组合
# dt = datetime.datetime(2019, 2, 16)
from datetime import datetime

dt = datetime(2019, 2, 16)
print(dt.today())
print(dt.now())

print(dt.fromtimestamp(time.time()))
print("-" * 100)


# datetime.timedelta: 表示一个时间间隔
from datetime import datetime, timedelta

t1 = datetime.now()
print(t1)
print(t1.strftime("%Y-%m-%d %H:%M:%S"))

# td表示一小时的时间长度
td = timedelta(hours=1)
# 当前时间加上时间间隔后，把得到的一个小时后的时间格式化输出
print((t1+td).strftime("%Y-%m-%d %H:%M:%S"))
