'''题 目 ： 输 入 某 年 某 月 某 日 ， 判 断 这 一 天 是 这 一 年 的 第 几 天 ？'''

import time
from datetime import date
# someday = input('请输入类似"%Y-%m-%d": ')
someday = "2020-8-20"
print("这是当年的第%s天。" % time.strptime(someday, '%Y-%m-%d')[7])


