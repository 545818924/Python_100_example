'''题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。'''

week = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']

while True:
    a = input("Enter first word(Q to quit): ")
    if a in ('q', 'Q'):
        break
    tmp = []
    for i in week:
        if a.upper() == i[0]:
            tmp.append(i)
    if len(tmp) == 1:
        print(tmp[0])
    else:
        a = input("Enter second word(Q to quit): ")
        if a in ('q', 'Q'):
            break     
        for i in tmp:
            if a.lower() == i[1]:
                print(i)
