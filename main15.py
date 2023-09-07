# Implementing queue using Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def EnQueue(self, data):
        temp = Node(data)
        if self.rear is None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp

    def Dequeue(self):
        if self.front is None:
            return
        temp = self.front
        self.front = temp.next

    def display(self):
        if self.front is None:
            return 'Empty'
        else:
            temp = self.front
            while temp is not None:
                print(temp.data)
                temp = temp.next
            print('***************************')


if __name__ == '__main__':
    q = Queue()
    q.EnQueue(5)
    q.EnQueue(5)
    q.EnQueue(5)
    q.display()
    q.Dequeue()
    q.display()
    q.Dequeue()
    q.display()
