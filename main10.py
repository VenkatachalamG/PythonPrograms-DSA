# Majority element of an array

def findMajority(arr, n):
    hashT = {}
    flag = 0
    for i in arr:
        if i in hashT:
            hashT[i] += 1
        else:
            hashT[i] = 1
    for i in hashT:
        if hashT[i] > n / 2:
            flag = 1
            print('Majority found :-', i)
    if flag == 0:
        print('No Majority')


arr = [2, 2, 2, 2, 5, 2, 5, 3, 3]
n = len(arr)
findMajority(arr, n)
