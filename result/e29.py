'''题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。'''

while True:
    try:
        number = input("请输入一个不多于五位的正整数（输入Q退出）： ")
        if number == 'Q':
            break
        if int(number):
            print("它的位数： ", len(number))
            print(number[::-1])
    except ValueError:
        print("输入错误请重新输入")
