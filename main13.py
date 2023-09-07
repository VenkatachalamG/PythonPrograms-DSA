# To delete the middle node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new

    def printlist(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next
        print('NULL')

    def deleteMid(self):
        slow = self.head
        fast = self.head
        prev = None
        while (fast is not None) and (fast.next is not None):
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next


linkedlist = LinkedList()
linkedlist.add(1)
linkedlist.add(2)
linkedlist.add(3)
linkedlist.add(4)

print('Before', end=" ")
linkedlist.printlist()
linkedlist.deleteMid()
print('After :', end=" ")
linkedlist.printlist()
