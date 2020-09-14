'''题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数'''

from random import randint
numbers = [randint(1, 100) for i in range(10)]
print(numbers)

m = int(input("Enter split index."))

a1 = numbers[:-m]
a2 = numbers[-m:]

new_m = a2 + a1

print(new_m)
