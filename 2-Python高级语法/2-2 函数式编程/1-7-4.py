# defaultdict

d1 = {"one":1, "two":2, "three":3}
print(d1["one"])
# print(d1["four"])，一般会直接报错

from collections import defaultdict

func = lambda: "May"
d2 = defaultdict(func)  # 调用不存在的属性时则调用函数func

d2["one"] = 1
d2["two"] = 2
print(d2)

print(d2["one"])
print(d2["four"])