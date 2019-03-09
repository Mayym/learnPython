# shelve忘记写回，需要使用强制写回
import shelve

shv = shelve.open(r'shv.db', writeback=True)
try:
    k1 = shv['one']
    print(k1)
    k1['eins'] = 100
finally:
    shv.close()

shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()
