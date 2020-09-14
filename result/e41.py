'''题目：模仿静态变量的用法。'''

s = 100


def get_num(n):
    global s
    return s * n


print(get_num(10))

