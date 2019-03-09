# 序列化案例
import pickle

age = 19
with open(r'test02.txt', 'wb') as f:
    pickle.dump(age, f)


# 反序列化案例
with open(r'test02.txt', 'rb') as f:
    age = pickle.load(f)
    print(age)