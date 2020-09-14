'''题目：列表排序及连接。'''

from random import randint

array = [randint(1, 100) for i in range(10)]

print(sorted(array))


array += [101]

print(array)
