# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''题 目 ： 暂 停 一 秒 输 出 ， 并 格 式 化 当 前 时 间 。  '''

import time
from datetime import datetime
for i in range(2):
    time.sleep(1)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
