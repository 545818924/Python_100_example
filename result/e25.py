'''题目：求1+2!+3!+...+20!的和。'''

res = 0
tmp = 1

for n, i in enumerate(range(1, 21), start=1):
    tmp *= i
    res += tmp
    print(f"第{n}的结果: {res}")
