# shelve忘记写回，需要使用强制写回
import shelve

shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库；解决办法：案例 2-4-5.py
    k1['eins'] = 100
finally:
    shv.close()


shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()
