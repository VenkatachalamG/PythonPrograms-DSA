# Largest node at each level

class newNode:
 
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def preOrder(root, level, lis):
    if root is None:
        return 0
    if level == len(lis):
        lis.append(root.data)
    else:
        lis[level] = max(lis[level], root.data)
    preOrder(root.left, level + 1, lis)
    preOrder(root.right, level + 1, lis)
    return lis
    
    
    
def largestValues(root):
    if root is None:
        return None
    level = 0
    lis = []
    return preOrder(root, level, lis)
         
# Driver Code
if __name__ == '__main__':
    """ Let us construct the following Tree
        4
        / \
        9 2
    / \ \
    3 5 7 """
    root = newNode(4)
    root.left = newNode(9)
    root.right = newNode(2)
    root.left.left = newNode(3)
    root.left.right = newNode(5)
    root.right.right = newNode(7)
    print(*largestValues(root))