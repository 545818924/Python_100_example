'''题 目 ： 输 入 三 个 整 数 x , y , z ， 请 把 这 三 个 数 由 小 到 大 输 出 。'''

list = []
for i in range(3):
    t = int(input("Enter number: "))
    list.append(t)

print(sorted(list))
