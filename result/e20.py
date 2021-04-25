'''题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？'''


def fall(height, n):
    return height * 1 / 2 ** n


res = height = 100
n = 10

for i in range(1, n):
	res += height 
	height /= 2



print(res)
print(fall(100, n))



