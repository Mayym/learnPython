# 序列化案例-2
import pickle

a = [23, 'May', 'I love studying', [160, 50]]

with open(r'test03.txt', 'wb') as f:
    pickle.dump(a, f)

with open(r'test03.txt', 'rb') as f:
    a = pickle.load(f)
    print(a)