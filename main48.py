# Inorder Traversal(Iterative)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    S = []
    cur = root
    while(1):
        if cur is not None:
            S.append(cur)
            cur = cur.left
        elif len(S):
            cur = S.pop()
            print(cur.data, end=" ")
            cur = cur.right
        else:
            break
if __name__ == '__main__':
     
    """ Constructed binary tree is
            1
          /   \
         2     3
       /  \
      4    5   """
     
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
     
    inOrder(root)
