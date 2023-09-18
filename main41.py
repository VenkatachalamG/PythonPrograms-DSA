#Mirror of a Tree
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
def inOrder(root):
    if root is None:
        return None
    else:
        temp = root
        inOrder(root.left)
        print(root.data, end=' ')
        inOrder(root.right)

def mirror(root):
    if root is None:
        return 0
    else:
        temp = root
        mirror(root.left)
        mirror(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp

if __name__ == "__main__":
 
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
 
    """ Print inorder traversal of
        the input tree """
    print("Inorder traversal of the",
          "constructed tree is")
    inOrder(root)
 
    """ Convert tree to its mirror """
    mirror(root)
 
    """ Print inorder traversal of
        the mirror tree """
    print("\nInorder traversal of",
          "the mirror tree is ")
    inOrder(root)