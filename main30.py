# Snake and Ladder Problem
def min_throw(N : int, arr : list[int]):
    t = [-1] * 31
    h = {}
    for i in range(0, 2 * N, 2):
        h[arr[i]] = arr[i + 1]
    return sol(1, h, t)


def sol(a: int, h: dict[int, int], t: list[int]):
    if a >= 30:
        return 0
    elif t[a] != -1:
        return t[a]
    minv = 999
    for j in range(1, 7):
        dice = a + j
        if dice in h:
            if h[dice] < dice:
                continue
            dice = h[dice]
        minv = min(minv, sol(dice, h, t) + 1)
    t[a] = minv
    return t[a]


N = 8
arr = [3, 22, 5, 8, 11, 26, 20, 29, 17, 4, 19, 7, 27, 1, 29, 9]
print("Min Dice throws required is", min_throw(N, arr))
