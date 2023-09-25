# Check for subtree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def preorder(root1, root2):
    if root1 is None and root2 is None or root1 is None or root2 is None:
        return False
    if root1.data == root2.data or (preorder(root1.left, root2.left) and preorder(root1.right, root2.right)):
        return True
    else:
        return False
def isSubtree(T, S):
    if T is None:
        return False
    if S is None:
        return False
    if preorder(T, S):
        return True
    elif preorder(T.left, S) or preorder(T.right, S):
        return True
    else:
        return False

    

        
T = Node(26)
T.right = Node(3)
T.right.right = Node(3)
T.left = Node(10)
T.left.left = Node(4)
T.left.left.right = Node(30)
T.left.right = Node(6)

S = Node(10)
S.right = Node(6)
S.left = Node(4)
S.left.right = Node(30)
 
if isSubtree(T, S):
    print("Tree 2 is subtree of Tree 1")
else:
    print("Tree 2 is not a subtree of Tree 1")
