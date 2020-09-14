'''题目：求100之内的素数。'''

for x in range(1, 101):
    t = 1
    for y in range(2, int(pow(x, 1 / 2)) + 1):
        if x % y == 0:
            t = 0
    if t:
        print(x)


res = [x for x in range(1, 101) if not [y for y in range(2, x) if x % y == 0]]
print(res)
