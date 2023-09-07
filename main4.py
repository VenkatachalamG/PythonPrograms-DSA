# Minimum Platforms
def findPlat(arr, dep, n):
    arr.sort()
    dep.sort()
    res = 1
    num = 1
    i = 1
    j = 0
    while i < n and j < n:
        if arr[i] > dep[j]:
            num = num - 1
            j = j + 1
        elif arr[i] <= dep[j]:
            num = num + 1
            i = i + 1
        if num > res:
            res = num
    return res


arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
n = len(arr)
print(findPlat(arr, dep, n))
