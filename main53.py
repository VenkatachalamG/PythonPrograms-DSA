# Kth Smallest/Largest element in an array
import heapq
def kthSmallest(arr, k):
    max_h = []
    for i in arr:
        heapq.heappush(max_h, -i)
        if len(max_h) > k:
            heapq.heappop(max_h)
    return -max_h[0]
if __name__ == "__main__":
    arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
    K = 4
 
    # Function call
    print("Kth Smallest Element is:", kthSmallest(arr, K))