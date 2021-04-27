'''题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。'''


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

while True:
	n = int(input("输入一个奇数： "))
	if n % 2 != 0:
		print(n  / gcd(n, 9))
	else:
		print('输入的不是奇数，请重新输入。')
