# Converting 2D Matrix into a LL
class Node:
    def __init__(self, data, next=None, down = None):
        self.data = data
        self.next = next
        self.down = down


def display(head):
    ptr = head
    temp = head
    while ptr is not None:
        temp = ptr
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
        ptr =ptr.down


def construct(arr, a, b, row, col, vis):
    if a > row - 1 or b > col - 1:
        return None
    if vis[a][b]:
        return vis[a][b]
    node = Node(arr[a][b])
    visited[a][b] = node

    node.next = construct(arr, a, b + 1, row, col, vis)
    node.down = construct(arr, a + 1, b, row, col, vis)
    return node


if __name__ == "__main__":
    # 2D matrix
    arr = [[1, 2, 3, 0],
           [4, 5, 6, 1],
           [7, 8, 9, 2],
           [7, 8, 9, 2]]
    m = 4
    n = 4
    visited = [[None] * n for _ in range(m)]
    head = construct(arr, 0, 0, m, n, visited)
    display(head)
