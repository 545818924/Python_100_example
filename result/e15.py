'''题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。'''
score = int(input("Enter the score: "))

if score >= 90:
    print("A")
elif score > 60:
    print("B")
else:
    print("C")


s_list = [[90, 'A'], [60, 'B'], [0, 'C']]
score = 70

for i in s_list:
    if score >= i[0]:
        print(i[1])
        break
