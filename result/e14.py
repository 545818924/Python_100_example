'''题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。'''
import time
import numpy as np


def run_time(func):
    def wrapper(*argv, **kwargv):
        t1 = time.time()
        print('*'.join(func(*argv, **kwargv)))
        t2 = time.time()
        print("Run time: ", t2 - t1)
    return wrapper


@run_time
def func(q, a=np.array([])):
    def Qnnn(q, a=np.array([])):
        for i in range(2, q + 1):
            if(q % i == 0):
                a = np.append(a, [str(i)])
                return (Qnnn(q // i, a))
                break
        return a
    return Qnnn(q, a=np.array([]))


@run_time
def func_(q, a=[]):
    def Qnnn(q, a=[]):
        for i in range(2, q + 1):
            if(q % i == 0):
                a.append(str(i))
                return (Qnnn(q // i, a))
                break
        return a
    return Qnnn(q, a=[])


# data = 25927169
data = 99099099000

func(data)
func_(data)

# t1 = time.time()
# print('the result is %s ' % '*'.join(Qnnn(data).tolist()))
# t2 = time.time()
# print("the runtime is %s" % (t2 - t1))
