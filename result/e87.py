'''题目：回答结果（结构体变量传递）。'''

def func(foo):
	def wrapper(*args, **kwargs):
		print('Begin')
		return foo(*args, **kwargs)
	return wrapper