'''题目：输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。'''


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(input("输入一个奇数： "))

print(n * 9 / gcd(n, 9))
