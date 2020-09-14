'''题目：找到年龄最大的人，并输出。请找出程序中有什么问题。'''

age_list = input("Enter age list: ").split(',')

print(max(int(i) for i in age_list))