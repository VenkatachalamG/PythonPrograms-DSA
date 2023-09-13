# Checking for BST
int_min = -999
int_max = 999
class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
def isBST(root):
   return checkId(root, int_min, int_max)

def checkId(root, mint, maxt):
   if root is None:
      return True
   if root.data < mint or root.data > maxt:
      return False
   return checkId(root.left, mint, root.data - 1) and checkId(root.right, root.data + 1, maxt)

if __name__ == "__main__":
  root = Node(4)
  root.left = Node(2)
  root.right = Node(5)
  root.left.left = Node(1)
  root.left.right = Node(3)
 
  # Function call
  if (isBST(root)):
      print("Is BST")
  else:
      print("Not a BST")