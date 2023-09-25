# Zigzag Traversal of a Tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    else:
 
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
 
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1

def zigzagtraversal(root):
    if root is None:
        return
 
    # Create an empty queue
    # for level order traversal
    cur = []
    nextl = []
    flag = True
    # Enqueue Root and initialize height
    cur.append(root)
    while(len(cur) > 0):
        # Print front of queue and
        # remove it from queue
        print(cur[-1].data, end=" ")
        node = cur.pop(-1)
        if flag:
            if node.left:
                nextl.append(node.left)
            if node.right:
                nextl.append(node.right)
        else:
            if node.right:
                nextl.append(node.right)
            if node.left:
                nextl.append(node.left)
        if len(cur) == 0:
            flag = False
            cur, nextl = nextl, cur

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(7)
root.left.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(4)
print("Zigzag Order traversal of binary tree is")
zigzagtraversal(root)