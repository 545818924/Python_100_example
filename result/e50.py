'''题目：输出一个随机数。'''

from random import *

print(random(), randint(1, 100), randrange(
    0, 100, 10), uniform(1, 10), sep='\n')
