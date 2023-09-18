#Dynamic Array

import math
import os
import random
import re
import sys
def dynamicArray(n, queries):
    arr = []
    res = []
    lostAnswer = 0
    for i in range(n):
        arr.append([])
        
    for i in range(len(queries)):
        if queries[i][0] == 1:
            x = queries[i][1]
            y = queries[i][2]
            idx = ((x^lostAnswer)%n)
            arr[idx].append(y)
        else:
            x = queries[i][1]
            y = queries[i][2]
            idx = ((x^lostAnswer)%n)
            lostAnswer = arr[idx][ y % len(arr[idx]) ]
            res.append(lostAnswer)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
