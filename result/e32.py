'''题目：按相反的顺序输出列表的值。'''

string = list('hello')
# 'h' in string

print(string[::-1])
print(list(reversed(string)))
# string.sort(key=lambda x: string.index(x), reverse=True)  # ValueError: 'h' is not in list  需查证
# print(string)

print(sorted(string, key=lambda x: string.index(x), reverse=True))
