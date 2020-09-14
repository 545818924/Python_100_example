'''题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？'''
from itertools import permutations

# 1
s = '1234'
t = 0
for i in permutations('1234', 3):
    print(''.join(i), end=',')
    t += 1
print('\n合计有%s个不重复的组合' % t)

# 2
res = [''.join((a, b, c)) for a in s for b in s for c in s if
       a != b and b != c and a != c]
print(len(res))
