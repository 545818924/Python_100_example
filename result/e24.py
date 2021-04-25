'''题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。'''


s = m = 1
res = 0
for n, i in enumerate(range(1, 21),start=1):
    s, m = m, s + m
    res += m / s
    print(n, " sum :%11.6f" % res)
