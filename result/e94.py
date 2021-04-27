'''题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。'''

import time
import random 


def guess_number(n):
    start = time.time()
    guess = int(input("Enter a number: "))
    while True:
        if guess == n:
            print("right !")
            break
        elif guess > n:
            print("Too big.")
        elif guess < n:
            print("Too small.")
        guess = int(input("Enter a number: "))
    end = time.time()
    print("User time: ", end - start)


guess_number(random.randint(1, 1000))
