# Reversing a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
        print('NULL')

    def reverseLL(self):
        cur = self.head
        prev = None
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def push(self, data):
        new_data = Node(data)
        new_data.next = self.head
        self.head = new_data


llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(150)
llist.push(200)
print('Before :', end=" ")
llist.printlist()
print('After :', end=" ")
llist.reverseLL()
llist.printlist()
