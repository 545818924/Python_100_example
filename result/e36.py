'''题目：求100之内的素数。'''

# solution 1 
for x in range(2, 101):
    t = 1
    for y in range(2, int(pow(x, 1 / 2)) + 1):
        if x % y == 0:
            t = 0
    if t:
        print(x, end=', ')

print('\n', '--' * 30)
# solution 2
res = [x for x in range(2, 101) if not [y for y in range(2, x) if x % y == 0]]
print(res)



print('--' * 30)
# solution 3 
tmp = list(range(2, 101))
for i in tmp:
	t = i
	while t <= 100:
		t += i
		if t in tmp:
			tmp.pop(tmp.index(t))

print(tmp)


