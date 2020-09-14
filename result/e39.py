'''题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。'''


from random import *

s = [randint(1, 101) for i in range(10)]
s.sort()
print(s)
num = int(input("Enter a number(1-100):"))

for n, i in enumerate(s):
    if num < i:
        s.insert(n, num)
        break
else:
    s.append(num)


print(s)
