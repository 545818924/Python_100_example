'''题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。'''

from random import randint


# array = [randint(1, 100) for i in range(10)]
array = [i for i in range(1, 11)]
print(array)


def ppp(array):
    if len(array) <= 2:
        return array[1]
    array = array[3:] + array[:2]
    print(array)
    return ppp(array)


print(ppp(array))
