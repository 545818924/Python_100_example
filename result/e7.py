# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''题 目 ： 将 一 个 列 表 的 数 据 复 制 到 另 一 个 列 表 中 。'''

# 浅拷贝
a = [1, 2, 3, [4]]
b = a[:]
a[-1].append(5)

print(a, id(a), b, id(b))

# 深拷贝
from copy import deepcopy

b = deepcopy(a)
a[-1].append(6)

print(a, id(a), b, id(b))
