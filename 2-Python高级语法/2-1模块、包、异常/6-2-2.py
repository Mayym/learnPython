import time

# strftime: 将时间元组转化为自定义的字符串格式
# 把时间表示成， 2019年2月16日 14:36
t = time.localtime()
# ft = time.strftime("%Y年%m月%d日 %H:%M", t)
# 含中文会报错：UnicodeEncodeError: 'locale' codec can't encode character '\u5e74' in position 2: encoding error
# 解决办法：
ft = time.strftime("%Y{y}%m{m}%d{d} %H:%M", t).format(y='年', m='月', d='日')
print(ft)
