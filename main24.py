# Adding two numbers represented by Linked List to store each digit of the operands
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def Sum(first, second):
    sumA = 0
    sum1 = 0
    while first.head is not None:
        sumA = (sumA * 10) + first.head.data
        first.head = first.head.next
    while second.head is not None:
        sum1 = (sum1 * 10) + second.head.data
        second.head = second.head.next
    total = sumA + sum1
    temp = LinkedList()
    while total != 0:
        num = total % 10
        temp.push(num)
        total = total // 10
    return temp


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        cur = Node(data)
        cur.next = self.head
        self.head = cur

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next


if __name__ == '__main__':
    first = LinkedList()
    second = LinkedList()
    first.push(6)
    first.push(8)
    first.push(6)
    first.push(9)
    first.push(4)
    first.push(5)
    first.push(2)

    second.push(2)
    second.push(3)
    result = Sum(first, second)
    result.printList()
