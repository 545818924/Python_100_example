'''题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。'''
import time

def check(n):
    t = []
    v = k = n
    for _ in range(1, v):
        if n % _ == 0:
            k -= _
            t.append(_)
    if k == 0:
        print(n, ":" , '+'.join([str(i) for i in t]))
        return True
    return False

[i for i in range(1,1001) if check(i)]
# print(s)