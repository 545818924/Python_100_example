'''题目：查找字符串。'''

import re

find_word = input("Enter you want to find words: ")
strings = 'Hello python!'

res = re.search(find_word, strings)
print(res.group(1)) if res else print("Not found")