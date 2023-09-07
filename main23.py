# Finding pairs in a DLL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def push(head, data):
    new = Node(data)
    if not head:
        head = new
    else:
        new.next = head
        head.prev = new
        head = new
    return head


def pairSum(head, x):
    first = head
    second = head
    while second.next is not None:
        second = second.next
    flag = False
    while first != second and second.next != first:
        if (first.data + second.data) == x:
            flag = True
            print('(', first.data, ', ', second.data, ')')
            first = first.next
            second = second.prev
        elif first.data + second.data > x:
            second = second.prev
        else:
            first = first.next
    if flag is False:
        print('No pair found')


if __name__ == '__main__':
    head = None
    head = push(head, 9)
    head = push(head, 8)
    head = push(head, 6)
    head = push(head, 5)
    head = push(head, 4)
    head = push(head, 2)
    head = push(head, 1)
    x = 7
    pairSum(head, x)
