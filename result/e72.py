'''题目：创建一个链表。'''


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

print(sample)
