'''题 目 ： 判 断 1 0 1 - 2 0 0 之 间 有 多 少 个 素 数 ， 并 输 出 所 有 素 数 。'''
import math

result = [x for x in range(101, 201) if not [y for y in range(
    2, int(math.sqrt(x)) + 1) if x % y == 0]]

print(result)


for x in range(101, 201):
    t = 1
    for y in range(2, int(pow(x, 1 / 2))):
        if x % y == 0:
            t = 0
            continue
    if t:
        print(x, end=',')
