'''题目：求1+2!+3!+...+20!的和。'''

res = 0
tmp = 1

for i in range(1, 21):
    tmp *= i
    res += tmp
    print(res)
