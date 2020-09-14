'''题目：反向输出一个链表。'''


class Node(object):
    """docstring for Node"""

    def __init__(self, value):
        self.value = value
        self.next = None


sample = []

for i in range(10):
    tmp = Node(i)
    tmp.next = Node(i + 1)
    sample.append(Node(i))

for i in sample:
    print(i)

print('---' * 30)
for i in sample[::-1]:
    print(i)
