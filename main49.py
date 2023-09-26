# Diameter of a Tree
class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def height(root, level):
    if root is None:
        return 0
    left_height = height(root.left, level)
    right_height = height(root.right, level)
  
    level[0] = max(level[0], 1 + left_height + right_height)
    return 1 + max(left_height, right_height)
def diameter(root):
    if root is None:
        return None
    level = [-999]
    height(root, level)
    return level[0]

if __name__ == '__main__':
    root = newNode(1) 
    root.left = newNode(2) 
    root.right = newNode(3) 
    root.left.left = newNode(4) 
    root.left.right = newNode(5) 
  
    print("Diameter is", diameter(root))