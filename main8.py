# Finding whether an array is subset of another array
def isSubset(arr1, arr2, m, n):
    arr1.sort()
    arr2.sort()
    if n > m:
        return 0
    i = 0
    j = 0
    while i < n and j < m:
        if arr2[j] < arr1[i]:
            j += 1
        elif arr2[j] == arr1[i]:
            j += 1
            i += 1
        elif arr2[j] > arr1[i]:
            return False
    return True


arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 1, 3, 7]

m = len(arr1)
n = len(arr2)
if isSubset(arr1, arr2, m, n):
    print("arr2[] is subset of arr1[] ")
elif not isSubset(arr1, arr2, m, n):
    print("arr2[] is not a subset of arr1[] ")
