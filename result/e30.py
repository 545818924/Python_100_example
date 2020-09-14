'''题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。'''


def palindrome(num):
    string = str(num)
    return string == string[::-1]


print(palindrome(98789))
