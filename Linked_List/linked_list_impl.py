class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None


n1 = Node(7)
n2 = Node(8)
n3 = Node(12)
n4 = Node(15)

ll = LinkedList()
n1.next = n2
n2.next = n3
n3.next = n4
ll.head = n1

print(ll.head.value)
print(ll.head.next.value)
print(ll.head.next.next.value)
print(ll.head.next.next.next.value)