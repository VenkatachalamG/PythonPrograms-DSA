# Sort a K-Sorted array using heap
import heapq

def sort_k(arr, n, k):
    heap = []
    heap = arr[:k + 1]
    target = 0

    for j in range(k + 1, n):
        arr[target] = heapq.heappop(heap)
        heapq.heappush(heap, arr[j])
        target += 1
    
    while heap:
        arr[target] = heapq.heappop(heap)
        target += 1

def print_array(arr: list):
    for elem in arr:
        print(elem, end=' ')
k = 3
arr = [2, 6, 3, 12, 56, 8]
n = len(arr)
sort_k(arr, n, k)
 
print_array(arr)