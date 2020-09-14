'''题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？'''


def fall(height, n):
    return height * 1 / 2 ** n


print(fall(100, 6))

n = 10
res = 0
height = 100

for i in range(1, 11):
    res += fall(n, i)
print(res)
print(fall(height, 10))


print([height * 1 / 2 ** i for i in range(1, i + 1)])
print(sum([height * 1 / 2 ** i for i in range(1, i + 1)]))
