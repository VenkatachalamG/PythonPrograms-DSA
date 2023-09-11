# Replace O's with X's
M = 6
N = 6


def replaceUtil(mat, x, y, new, prev):
    if x < 0 or x >= M - 1 or y < 0 or y >= N - 1 or mat[x][y] != prev:
        return

    mat[x][y] = new

    replaceUtil(mat, x + 1, y, new, prev)
    replaceUtil(mat, x - 1, y, new, prev)
    replaceUtil(mat, x, y + 1, new, prev)
    replaceUtil(mat, x, y - 1, new, prev)


def replaceSurrounded(mat):
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 'O':
                mat[i][j] = '-'
    for i in range(N):
        if mat[0][i] == '-':
            replaceUtil(mat, 0, i, 'O', '-')
        elif mat[M-1][i]:
            replaceUtil(mat, M - 1, i, 'O', '-')
    for i in range(M):
        if mat[i][0] == '-':
            replaceUtil(mat, i, 0, 'O', '-')
        elif mat[i][N-1] == '-':
            replaceUtil(mat, i, N - 1, 'O', '-')


    for i in range(M):
        for j in range(N):
            if mat[i][j] == '-':
                mat[i][j] = 'X'


if __name__ == '__main__':

    mat = [['X', 'O', 'X', 'O', 'X', 'X'],
           ['X', 'O', 'X', 'X', 'O', 'X'],
           ['X', 'X', 'X', 'O', 'X', 'X'],
           ['O', 'X', 'X', 'X', 'X', 'X'],
           ['X', 'X', 'X', 'O', 'X', 'O'],
           ['O', 'O', 'X', 'O', 'O', 'O']];

    replaceSurrounded(mat)

    for i in range(M):
        print(*mat[i])
