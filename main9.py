# Find maximum product subarray

def maxSubarrayProduct(arr, n):
    max1 = arr[0]
    min1 = arr[0]
    maxp = arr[0]

    for i in range(1, n):
        temp = max(max(arr[i], arr[i] * max1), arr[i] * min1)
        min1 = min(min(arr[i], arr[i] * max1), arr[i] * min1)
        max1 = temp
        maxp = max(max1, min1)
    return maxp


arr = [1, -2, -3, 5, -8]
n = len(arr)
print("Maximum Sub array product is", maxSubarrayProduct(arr, n))
