'''题 目 ： 打 印 出 所 有 的 " 水 仙 花 数 " ， 所 谓 " 水 仙 花 数 " 是 指 一 个 三 位 数 ， 其 各 位 数 字 立 方 和 等 于 该 数 本 身 。
 例 如 ： 1 5 3 是 一 个 " 水 仙 花 数 " ， 因 为 1 5 3 = 1 的 三 次 方 ＋ 5 的 三 次 方 ＋ 3 的 三 次 方 。'''

for x in range(100, 1000):
    t = 0
    for y in str(x):
        t += int(y) ** 3
    if t == x:
        print(x)


for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            if pow(i, 3) + pow(j, 3) + pow(k, 3) == i * 100 + j * 10 + k:
                print(i, j, k)
