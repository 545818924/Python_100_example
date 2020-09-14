'''题 目 ： 斐 波 那 契 数 列 。  '''


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

print(fib(10))
