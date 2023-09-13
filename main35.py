#Fnding Height of a tree
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
def maxDepth(root):
    if root is None:
        return 0
    else:
        lDepth = maxDepth(root.left)
        rDepth = maxDepth(root.right)
    return max(lDepth, rDepth) + 1



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
 
 
print("Height of tree is ", maxDepth(root))