'''题目：读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊。'''

from random import randint


[print('*' * randint(1, 50)) for i in range(7)]
