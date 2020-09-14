'''题目：字符串排序。'''

print(sorted(input("Enter strings: ").split(','), key=lambda x:int(x)))