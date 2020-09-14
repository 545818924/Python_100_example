'''题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。'''


class Counter_string():
    def counter(self, string):
        dic = dict(alpha=0,
                   digit=0,
                   space=0,
                   other=0)
        for s in string:
            if s.isalpha():
                dic['alpha'] += 1
            elif s.isdigit():
                dic['digit'] += 1
            elif s.isspace():
                dic['space'] += 1
            else:
                dic['other'] += 1
        return dic


c = Counter_string()
string = 'Hello, Python! today is 2020-04-29.'
# string = '1234566'
print(c.counter(string))
