# To check for children sum property
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isSumProperty(root):
    leftd = 0
    rightd = 0
    if root is None or (root.right is None and root.left is None):
        return 1
    else:
        if root.left is not None:
            leftd = root.left.data
        if root.right is not None:
            rightd = root.right.data
        if root.data == leftd + rightd and (isSumProperty(root.left) and isSumProperty(root.right)):
            return 1
        else:
            return 0        

if __name__ == '__main__':
    root = newNode(10)
    root.left = newNode(8)
    root.right = newNode(2)
    root.left.left = newNode(3)
    root.left.right = newNode(5)
    root.right.right = newNode(2)
 
    # Function call
    if(isSumProperty(root)):
        print("The given tree satisfies the",
              "children sum property ")
    else:
        print("The given tree does not satisfy",
              "the children sum property ")