'''题目：画图，学用rectangle画方形。'''

from turtle import *


def rectangle(n):
    for i in range(4):
        fd(n)
        right(90)


rectangle(100)
