'''题目：求一个3*3矩阵主对角线元素之和。'''

from random import *

res = [[randint(1, 10) for i in range(3)]for i in range(3)]
s = 0
for i in range(3):
    for j in range(3):
        if i % 2 == 0 and j % 2 == 0 or i == j:
            s += res[i][j]


print(res, s)
