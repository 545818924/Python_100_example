'''题目：利用递归方法求5!。'''


def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n


print(factorial(5))
