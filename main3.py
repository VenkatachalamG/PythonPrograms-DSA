# Arranging array in alt -VE and +VE elements
def altPosNeg(arr, n):
    flag = -1
    for i in range(n):
        if flag >= 0:
            if (arr[i] >= 0 and arr[flag] < 0) or (arr[i] < 0 and arr[flag] > 0):
                ans = rightRot(arr, i, flag)
                if i - flag > 2:
                    flag += 2
                else:
                    flag = -1
        if flag == -1:
            if (arr[i] >= 0 and i % 2 == 0) or (arr[i] < 0 and i % 2 == 1):
                flag = i
    return ans


def rightRot(arr, i, flag):
    temp = arr[i]
    for j in range(i, flag, -1):
        arr[j] = arr[j - 1]
    arr[flag] = temp
    return arr


arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print("Given Array is:")
print(arr)
n = len(arr)
print("\nRearranged array is:")
print(altPosNeg(arr, n))
