# calendar： 获取一年的日历字符串
# 参数：
# w = 每个日期之间的间隔字符数
# l = 每周所占用的行数
# c = 每个月之间的间隔字符数
import calendar

cal = calendar.calendar(2019)
print(type(cal))
print(cal)
print("-" * 100)

cal = calendar.calendar(2019, l=0, c=5)
print(cal)
print("-" * 100)


# isleap: 判断某一年是否闰年
print(calendar.isleap(2019))
print(calendar.isleap(2020))


# leapdays: 获取指定年份之间的闰年的个数
print(calendar.leapdays(2001, 2018))
print("*" * 100)
help(calendar.leapdays)
print("*" * 100)
print(calendar.leapdays(2018, 2001))  # 返回-4
print("-" * 100)


# month(): 获取某个月的日历字符串
# 格式： calendar.month(年，月)
# 回值： 月日历的字符串
print(calendar.month(2019, 2))
print("*" * 100)


# monthrange(): 获取一个月的周几开始即和天数
# 格式： calendar.monthrange(年，月)
# 回值： 元组（周几开始，总天数）
# 注意： 周默认0-6表示周一到周天
help(calendar.monthrange)
print("*" * 100)

print(calendar.monthrange(2019, 2))

w, t = calendar.monthrange(2019, 2)
print(w)
print(t)
print("-" * 100)


# monthcalendar() 返回一个月每天的矩阵列表
# 格式： calendar.monthcalendar(年，月)
# 回值： 二级列表
# 注意： 矩阵中没有天数用0表示
m = calendar.monthcalendar(2019, 2)
print(type(m))
print(m)
print("-" * 100)


# prcal: print calendar直接打印日历
calendar.prcal(2019)
print("*" * 100)
help(calendar.prcal)
print("*" * 100)


# prmonth() 直接打印整个月的日历
# 格式： calendar.prmonth(年，月)
# 返回值： 无
calendar.prmonth(2019, 2)
print("-" * 100)


# weekday() 获取周几
# 格式： calendar.weekday(年，月，日)
# 返回值： 周几对应的数字
print(calendar.weekday(2019, 2, 15))
