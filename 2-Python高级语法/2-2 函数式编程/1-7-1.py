# zip案例
l1 = [1,2,3,4,5]
l2 = [11,22,33,44,55]

z = zip(l1, l2)

print(type(z))
print(z)

for i in z:
    print(i)


# zip案例-2
l1 = ['may', 'zym', 'Angela']
l2 = [89, 56, 98]

z = zip(l1, l2)

'''for i in z:
    print(i)'''


l3 = [i for i in z]
print(l3)