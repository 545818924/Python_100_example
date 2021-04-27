'''题目：编写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n'''


n = int(input("Enter a number: "))


n = 88
s = 0
while n > 0:
    t = 1 / (n)
    n -= 2
    s += t

print(s)
