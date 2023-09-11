# Flood Fill Algorithm
M = 8
N = 8


def floodFill(screen, x, y, newC):
    prev = screen[x][y]
    if screen[x][y] == newC:
        return
    floodFillAlg(screen, x, y, newC, prev)


def floodFillAlg(screen, x, y, newC, prev):
    if 0 < x >= M or 0 < y >= N or screen[x][y] != prev or screen[x][y] == newC:
        return
    screen[x][y] = newC
    floodFillAlg(screen, x, y + 1, newC, prev)
    floodFillAlg(screen, x, y - 1, newC, prev)
    floodFillAlg(screen, x + 1, y, newC, prev)
    floodFillAlg(screen, x - 1, y, newC, prev)


screen = [[1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 0, 0],
          [1, 0, 0, 1, 1, 0, 1, 1],
          [1, 2, 2, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 0, 1, 0],
          [1, 1, 1, 2, 2, 2, 2, 0],
          [1, 1, 1, 1, 1, 2, 1, 1],
          [1, 1, 1, 1, 1, 2, 2, 1]]

x = 4
y = 4
newC = 3
floodFill(screen, x, y, newC)

print("Updated screen after call to floodFill:")
for i in range(M):
    for j in range(N):
        print(screen[i][j], end=' ')
    print()
