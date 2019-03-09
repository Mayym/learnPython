# shelve之只读打开
import shelve

shv = shelve.open(r'shv.db', flag='r')

try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()
