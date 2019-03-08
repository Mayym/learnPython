import functools
# 实现int16的功能
int16 = functools.partial(int, base=16)

print(int16("12345"))