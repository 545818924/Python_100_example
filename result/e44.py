'''两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：'''


from random import *

a = [[randint(1, 100) for i in range(3)]for i in range(3)]
b = [[randint(1, 100) for i in range(3)]for i in range(3)]

c = []

c = [[a[x][y] + b[x][y] for x in range(3)]for y in range(3)]

print(a, b, c, sep='\n')
