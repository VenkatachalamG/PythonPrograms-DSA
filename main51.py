# Check if performing preorder traversal of an array form a BST 
int_min = -9999999999999

def canRepresentBST(arr):
    stack = []
    root = int_min
    for i in arr:
        if i < root:
            return False
        while len(stack) > 0 and i > stack[-1]:
            root = stack.pop()
        stack.append(i)
    return True
pre1 = [40 , 30 , 35 , 80 , 100]
print ("true" if canRepresentBST(pre1) == True else "false")
pre2 = [40 , 30 , 35 , 20 ,  80 , 100]
print ("true" if canRepresentBST(pre2) == True else "false")