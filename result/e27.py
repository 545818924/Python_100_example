'''题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。'''

def reverse(string):
	if len(string) == 1:
		return string
	return string[-1] + reverse(string[:-1])


print(reverse('hello'))
