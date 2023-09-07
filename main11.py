# Implementing two stacks in an array
import math


class twoStacks:

    def __init__(self, n):  # constructor
        self.size = n
        self.arr = [None] * n
        self.top1 = math.floor(n / 2) + 1
        self.top2 = math.floor(n / 2)

    def push1(self, x):
        if self.top1 > 0:
            self.top1 = self.top1 - 1
            self.arr[self.top1] = x
        else:
            print("Stack Overflow by element : ", x)

    def push2(self, x):

        # There is at least one empty space for new element
        if self.top2 < self.size - 1:
            self.top2 = self.top2 + 1
            self.arr[self.top2] = x
        else:
            print("Stack Overflow by element : ", x)

    def pop1(self):
        if self.top1 <= self.size / 2:
            x = self.arr[self.top1]
            self.top1 = self.top1 + 1
            return x
        else:
            print("Stack Underflow")
            exit(1)

    def pop2(self):
        if self.top2 >= math.floor(self.size / 2) + 1:
            x = self.arr[self.top2]
            self.top2 = self.top2 - 1
            return x
        else:
            print("Stack Underflow")
            exit(1)


if __name__ == '__main__':
    ts = twoStacks(5)
    ts.push1(5)
    ts.push2(10)
    ts.push2(15)
    ts.push1(11)
    ts.push2(7)

    print("Popped element from stack1 is : " + str(ts.pop1()))
    ts.push2(40)
    print("Popped element from stack2 is : " + str(ts.pop2()))
