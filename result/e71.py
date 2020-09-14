'''题目：编写input()和output()函数输入，输出5个学生的数据记录。'''

res = [{"name": input("Enter name: "), "id_num": input("Enter id: ")}
       for i in range(3)]


print(res)
