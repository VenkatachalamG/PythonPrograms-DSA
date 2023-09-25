# Array to BST
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sortedArrayToBST(arr):
    if not arr:
        return None
    m = len(arr) // 2
    root = Node(arr[m])
    root.left = sortedArrayToBST(arr[:m])
    root.right = sortedArrayToBST(arr[m + 1:])
    return root

def preOrder(node):
    if not node:
        return
 
    print(node.data,)
    preOrder(node.left)
    preOrder(node.right)

arr = [1, 2, 3, 4, 5, 6, 7]
root = sortedArrayToBST(arr)
print("PreOrder Traversal of constructed BST ", preOrder(root))