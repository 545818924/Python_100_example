'''题目：时间函数举例1。'''

import time

print(time.asctime())
print(time.strptime(time.asctime(),'%c'))
