# Minimum distance between two nodes in a tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def findPath(root, path, val):
    if root is None:
        return 0
    path.append(root.data)
    if root.data == val:
        return True
    if (root is not None and findPath(root.left, path, val)) or (root is not None and findPath(root.right, path, val)):
        return True
    path.pop()
    return False
def distance(root, start, end):
    if root is not None:
        p1 = []
        findPath(root, p1, start)

        p2 = []
        findPath(root, p2, end)

        i = 0
        while i< len(p1) and i < len(p2):
            if p1[i] != p2[i]:
                break
            i = i + 1
        return (len(p1) + len(p2)) - 2 * i
    else:
        return 0 
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right= Node(7)
root.right.left = Node(6)
root.left.right = Node(5)
root.right.left.right = Node(8)
 
dist = distance(root, 3, 5)
print ("Distance between node {} & {}: {}".format(3, 5, dist))
 
dist = distance(root, 4, 6)
print ("Distance between node {} & {}: {}".format(4, 6, dist))
 
dist = distance(root, 3, 4)
print ("Distance between node {} & {}: {}".format(3, 4, dist))
 
dist = distance(root, 2, 4)
print ("Distance between node {} & {}: {}".format(2, 4, dist))
 
dist = distance(root, 8, 5)
print ("Distance between node {} & {}: {}".format(8, 5, dist))