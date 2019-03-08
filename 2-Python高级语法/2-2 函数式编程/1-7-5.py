# Counter
from collections import Counter

# 为什么下面结果不把"abcdefgabcdeabcdabcaba"作为键值，而是以其中每一个字母作为键值
# 因为需要括号里内容为可迭代
c = Counter("abcdefgabcdeabcdabcaba")
print(c)

s = ["May", "love", 'love', "love", 'playing computer game']
c = Counter(s)
print(c)