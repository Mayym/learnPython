import shelve

shv = shelve.open(r'shv.db')
try:
    shv['one'] = {'eins':1, 'zwei':2, 'drei':3}
finally:
    shv.close()

shv = shelve.open(r'shv.db')
try:
    one = shv['one']
    print(one)
finally:
    shv.close()