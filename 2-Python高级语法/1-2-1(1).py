def f(x):
    return x * x

r = map(f, [1,2,3,4,5,6,7,8,9])
print(list(r))

l = [i for i in range(1, 10)]
s = map(f, l)
print(list(s))
