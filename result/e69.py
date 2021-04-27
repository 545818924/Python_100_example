'''题目：有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。'''

from pythonds.basic import Queue
from random import randint

# solution 1
array = [i for i in range(1, 11)]
print(array)


def ppp(array, n):
    print(array)
    if len(array) <= 2:
        return array[1]
    array = array[n:] + array[:n-1]
    return ppp(array, n)


print(ppp(array, 3))


# solution 2
def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())

        simqueue.dequeue()

    return simqueue.dequeue()

# tmp = ["Bill","David","Susan","Jane","Kent","Brad"]


# print(hotPotato(tmp, 7))
print(hotPotato(array, 2))
