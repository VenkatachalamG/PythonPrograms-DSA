# Finding common elements in 3 arrays
def intersect(arr1, arr2):
    if len(arr1) < len(arr2):
        arr1, arr2 = arr2, arr1
    freq = {}
    for i in arr1:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1
    lis = []
    for i in arr2:
        if i in freq and freq[i]:
            freq[i] -= 1
            lis.append(i)
    return lis


def findCommon(ar1, ar2, ar3):
    lis1 = intersect(ar1, ar2)
    lis2 = intersect(ar2, ar3)
    return lis2


ar1 = [1, 15, 10, 20, 40, 80]
ar2 = [6, 7, 20, 15]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
n1 = len(ar1)
n2 = len(ar2)
n3 = len(ar3)
print("Common elements are", findCommon(ar1, ar2, ar3))
