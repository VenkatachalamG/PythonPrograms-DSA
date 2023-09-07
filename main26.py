# Converting a binary tree into a doubly linked list of spiral fashion
class newNode:

    # Constructor to create a newNode
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


""" Given a reference to the head of a list
    and a node, inserts the node on the front
    of the list. """


# Function to prints contents of DLL
def printList(node):
    i = 0
    while (i < len(node)):
        print(node[i].data, end=" ")
        i += 1


""" Function to print corner node at each level """


def spiralLevelOrder(root):
    # Base Case
    if (root == None):
        return

    # Create an empty deque for doing spiral
    # level order traversal and enqueue root
    q = []
    q.append(root)

    # create a stack to store Binary
    # Tree nodes to insert into DLL later
    stk = []

    level = 0
    while (len(q)):

        # nodeCount indicates number of
        # Nodes at current level.
        nodeCount = len(q)

        # Dequeue all Nodes of current level
        # and Enqueue all Nodes of next level
        if (level & 1):  # odd level
            while (nodeCount > 0):

                # dequeue node from front &
                # push it to stack
                node = q[0]
                q.pop(0)
                stk.append(node)

                # insert its left and right children
                # in the back of the deque
                if (node.left != None):
                    q.append(node.left)
                if (node.right != None):
                    q.append(node.right)

                nodeCount -= 1

        else:  # even level

            while (nodeCount > 0):

                # dequeue node from the back &
                # push it to stack
                node = q[-1]
                q.pop(-1)
                stk.append(node)

                # inserts its right and left
                # children in the front of
                # the deque
                if (node.right != None):
                    q.insert(0, node.right)
                if (node.left != None):
                    q.insert(0, node.left)
                nodeCount -= 1
        level += 1

    # head pointer for DLL
    head = []

    # pop all nodes from stack and push
    # them in the beginning of the list
    while (len(stk)):
        head.append(stk[0])
        stk.pop(0)

    print("Created DLL is:")
    printList(head)


# Driver Code
if __name__ == '__main__':
    """Let us create Binary Tree as 
    shown in above example """

    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)

    root.left.left.left = newNode(8)
    root.left.left.right = newNode(9)
    root.left.right.left = newNode(10)
    root.left.right.right = newNode(11)
    # root.right.left.left = newNode(12)
    root.right.left.right = newNode(13)
    root.right.right.left = newNode(14)
    # root.right.right.right = newNode(15)

    spiralLevelOrder(root)
