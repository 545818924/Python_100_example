# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''题 目 ： 输 出   9 * 9   乘 法 口 诀 表 。'''

print('\n'.join(['\t'.join(["{} * {} = {}".format(y, x, x*y)for y in range(1, x+1)])for x in range(1, 10)]))

print('\n'.join(['\t'.join(["{:d} * {:d} = {:<2d}".format(y, x, y*x) for y in range(1, x+1)])for x in range(1, 10)]))