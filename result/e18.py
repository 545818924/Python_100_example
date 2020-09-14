'''题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。'''


def re_add(num, length):
    pattern = [str(num) * i for i in range(1, length + 1)]
    return "%s=%s" % (('+'.join(pattern)), eval(('+'.join(pattern))))


print(re_add(1, 9))
