'''题目：文本颜色设置。'''


class bcolor():
    HEADER = '\033[1; 45m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


print(bcolor.WARNING + 'WARNING: start httpd failed' + bcolor.ENDC)
print(bcolor.OKGREEN + 'start  ……' + bcolor.ENDC)

s = input()
