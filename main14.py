# Circular Linked List traversal
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLL:
    def __init__(self):
        self.head = None

    def push(self, data):
        cur = Node(data)
        temp = self.head
        cur.next = self.head
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = cur
        else:
            cur.next = cur
        self.head = cur

    def printList(self):
        temp = self.head
        while True:
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                break


link = CircularLL()
link.push(10)
link.push(40)
link.push(60)
link.push(90)
link.push(7)
print('The circular linked list is :')
link.printList()
