# Inorder Successor of a node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


def inOrderTraversal(root, temp, nroot):
    if(root == None): return
    inOrderTraversal(root.left, temp, nroot)
    if(root.data > temp.data and not nroot.left):
        nroot.left = root
        return
    inOrderTraversal(root.right, temp, nroot) 


def inOrderSuccessor(root, temp):
    nroot = Node(0)
    inOrderTraversal(root, temp, nroot)
    return nroot.left

def insert(node, data):
    if (node == None):
        return Node(data)
    else:
        if (data <= node.data):
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node
        return node
    
root = None
root = insert(root, 20)
root = insert(root, 8)
root = insert(root, 22)
root = insert(root, 4)
root = insert(root, 12)
root = insert(root, 10)
root = insert(root, 14)
temp = root.left.right.right
 
succ = inOrderSuccessor(root, temp)
if (succ != None): print("Inorder Successor of",temp.data,"is",succ.data)
else: print("Inorder Successor doesn't exist")
