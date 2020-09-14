'''题目：输出一个随机数。'''

from random import *

print(random(), randint(1, 100), randrange(
    1, 100, 2), uniform(1, 10), sep='\n')
