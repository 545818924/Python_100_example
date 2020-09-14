'''题目：打印出杨辉三角形（要求打印出10行如下图）。'''

s1 = [1]
res = []

for i in range(10):
    res.append(s1)
    s2 = []
    s1 = [0] + s1 + [0]
    for t in range(len(s1) - 1):
        s2.append(s1[t] + s1[t + 1])
    s1 = s2


for i in res:
    print(i)
