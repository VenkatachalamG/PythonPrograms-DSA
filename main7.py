#Triplet Sum in Array
def find3Numbers(arr, n, sum):
    arr.sort()
    for i in range(0, n - 2):
        j = i + 1
        k = n - 1
        while j < k:
            if arr[i] + arr[j] + arr[k] < sum:
                i = i + 1
            elif arr[i] + arr[j] + arr[k] > sum:
                k = k - 1
            elif sum == arr[j] + arr[k] + arr[i]:
                print('Triplet :', arr[i], arr[j], arr[k])
                return


A = [1, 4, 45, 6, 10, 8]
sum = 22
arr_size = len(A)

find3Numbers(A, arr_size, sum)
