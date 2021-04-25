'''题目：打印出如下图案（菱形）:'''


# res = ["*" * 11 for i in range(9)]
# print(res)
# m = 19
# mid = m // 2
# temp = []
# star = '*'
# for i in range(m - mid):
#     mid_s = mid - i
#     mid_p = mid + i
#     t = list(' ' * m)
#     t[mid_s] = star
#     t[mid_p] = star
#     # ''.join(t)
#     temp.append(t)

# for i in range(m - 1 - mid - 1, -1, -1):
#     mid_s = mid - i
#     mid_p = mid + i
#     t = list(' ' * m)
#     t[mid_s] = star
#     t[mid_p] = star
#     # ''.join(t)
#     temp.append(t)

# for i in temp:
#     print(''.join(i))

m = 19
print('*'.center(m))
for i in range(1, m, 2):
    print(('*' + ' ' * i + '*').center(m))
for i in range(m - 4, -1, -2):
    print(('*' + ' ' * i + '*').center(m))
print('*'.center(m))
