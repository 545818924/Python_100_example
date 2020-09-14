'''题目：求输入数字的平方，如果平方运算后小于 50 则退出。'''


import sys

a = input("a number：")
res = pow(int(a), 2)
print(res) if res >= 50 else sys.exit(-1)
