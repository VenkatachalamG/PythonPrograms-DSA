#Spiral form of an array
def spiralOrder(arr):
    lis = []
    seen = [[0 for i in range(len(arr[0]))] for j in range(len(arr))]
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            seen[r][c] = 0
    x = 0
    y = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    di = 0

    for i in range(len(arr[0])*len(arr)):
        lis.append(arr[x][y])
        seen[x][y] = 1

        cr = x + dr[di]
        cc = y + dc[di]

        if (0 <= cr < len(arr)) and (0 <= cc < len(arr[0])) and not seen[cr][cc]:
            x = cr
            y = cc
        else :
            di = (di + 1) % 4
            x += dr[di]
            y += dc[di]
    return lis


if __name__ == "__main__":
    a = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12]]

    # Function call
    for x in spiralOrder(a):
        print(x, end=" ")