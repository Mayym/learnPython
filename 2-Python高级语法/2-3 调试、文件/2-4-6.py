# shelve使用with管理上下文环境
import shelve


with shelve.open(r'shv.db', writeback=True) as shv:
    k1 = shv['one']
    print(k1)
    k1['eins'] = 1000

with shelve.open(r'shv.db') as shv:
    print(shv['one'])
