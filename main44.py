#Lowest Common Ancestor of a BST
class Node:
     def __init__(self, data):
          self.data = data
          self.left = None
          self.right = None
def lca(root, v1, v2):
  if root is None:
       return None
  mini = min(v1, v2)
  maximum = max(v1, v2)
  if root.data == v1 or root.data == v2:
        return root
  left_lca = lca(root.left, v1, v2)
  right_lca = lca(root.right, v1, v2)
  if left_lca and right_lca:
        return root
  return left_lca if left_lca is not None else right_lca

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print("LCA(4, 5) = ", lca(root, 4, 5).data)
    print("LCA(4, 6) = ", lca(root, 4, 6).data)
    print("LCA(3, 4) = ", lca(root, 3, 4).data)
    print("LCA(2, 4) = ", lca(root, 2, 4).data)
