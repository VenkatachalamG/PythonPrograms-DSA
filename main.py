# QuickSort Algorithm
def quicksort(a, start, end):
    if start < end:
        p = partition(a, start, end)
        quicksort(a, start, p - 1)
        quicksort(a, p + 1, end)


def partition(a, start, end):
    pivot = a[end]
    j = start - 1
    for k in range(start, end):
        if a[k] <= pivot:
            j += 1
            a[j], a[k] = a[k], a[j]
    a[j + 1], a[end] = a[end], a[j + 1]
    return j + 1


arr = [10, 80, 30, 90, 40, 50, 70]
n = len(arr)
print('Before Sort :', arr)
quicksort(arr, 0, n - 1)
print('After Sort', arr)
