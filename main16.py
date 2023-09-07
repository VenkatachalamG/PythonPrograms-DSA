# Remove every kth-node from a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def freeList(node):
    while node is not None:
        next = node.next
        node = next
    return node


def deleteKthNode(head, k):
    if head is None:
        return None

    if k == 1:
        freeList(head)
        return None
    ptr = head
    prev = None
    count = 0
    while ptr is not None:
        count = count + 1

        if k == count:
            prev.next = ptr.next
            count = 0

        if count != 0:
            prev = ptr

        ptr = prev.next

    return head


def displayList(head):
    temp = head
    while temp is not None:
        print(temp.data, end=' ')
        temp = temp.next


def newNode(x):
    temp = Node(x)
    temp.data = x
    temp.next = None
    return temp


if __name__ == '__main__':
    head = newNode(1)
    head.next = newNode(2)
    head.next.next = newNode(3)
    head.next.next.next = newNode(4)
    head.next.next.next.next = newNode(5)
    head.next.next.next.next.next = newNode(6)
    head.next.next.next.next.next.next = newNode(7)
    head.next.next.next.next.next.next.next = newNode(8)

    k = 2
    head = deleteKthNode(head, k)

    displayList(head)