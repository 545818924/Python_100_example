'''题目：字符串日期转换为易读的日期格式。'''


from datetime import datetime

today = datetime.today()

print(today.strftime('%Y-%m-%d'))
