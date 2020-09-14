'''题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。'''

import time


def check(n):
    v = k = n
    for _ in range(1, v):
        if n % _ == 0:
            k -= _
            # print(n, _, k)
    if k == 0:
        return True
    return False


t3 = time.time()
for i in range(1, 1000):
    if check(i):
        print(i)
t4 = time.time()

print("2. ", (t4 - t3))


def prime(n):
    t = True
    for i in range(2, int(pow(n, 1 / 2)) + 1):
        if n % i == 0:
            t = False
    return t


t1 = time.time()
for i in range(2, 10):
    if prime(i):
        s = (pow(2, i) - 1) * (pow(2, i - 1))
        if s > 1000:
            break
        print(s)
t2 = time.time()
print('1. ', t2 - t1)
