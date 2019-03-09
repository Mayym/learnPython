# shelve读取案例
import shelve

shv = shelve.open(r'shv.db')

try:
    print(shv['one'])
    print(shv['three'])
    print(shv['four'])
except Exception as e:
    print('报错了')
finally:
    shv.close()
