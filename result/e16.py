'''题目：输出指定格式的日期。'''

from datetime import datetime

print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))