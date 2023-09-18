#Printing top view of a Tree


def topView(root):
    #Write your code here
    if root == None:
        return
    q = []
    m = dict()
    level = 0
    root.level = level

    # push node and horizontal
    # distance to queue
    q.append(root)

    while len(q):
        root = q[0]
        level = root.level

        # count function will return 1 if the container has an element whose key            is equal to level otherwise it will return zero.
        if level not in m:
            m[level] = root.info
        if root.left:
            root.left.level = level - 1
            q.append(root.left)

        if root.right:
            root.right.level = level + 1
            q.append(root.right)

        q.pop(0)
    for i in sorted(m):
        print(m[i], end=" ")

