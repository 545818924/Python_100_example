# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''题 目 ： 古 典 问 题 ： 有 一 对 兔 子 ， 从 出 生 后 第 3 个 月 起 每 个 月 都 生 一 对 兔 子 ， 小 兔 子 长 到 第 三 个 月 后 每 个 月 又 生 一 对 兔 子 ， 假 如 兔 子 都 不 死 ， 问 每 个 月 的 兔 子 总 数 为 多 少 ？  '''


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_(n):
    a, b = 0, 1
    t = 0
    while t < n:
        result = b
        a, b = b, a + b
        t += 1
    return result


n = 10
print(fib_(n))
print(fib(n))  # 总数需乘2
