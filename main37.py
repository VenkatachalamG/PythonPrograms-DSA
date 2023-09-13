# Checking for symetric tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def isMirror(root1, root2):
    if root1 is None and root2 is None:
        return 1
    if root1 is not None and root2 is not None:
        if root1.data == root2.data:
            return isMirror(root1.left, root2.right) and isMirror(root1.right, root2.left)
    return 0
def isSymmetric(root):
 
    # Check if tree is mirror of itself
    return isMirror(root, root)
 
 
# Driver Code
# Let's construct the tree show in the above figure
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)
print ("Symmetric" if isSymmetric(root) == True else "Not symmetric")