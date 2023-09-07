# Stock Span Problem
def calculateSpan(price, S):
    s = []
    s.append(0)
    S[0] = 1
    for i in range(len(price)):
        while len(s) > 0 and price[s[-1]] <= price[i]:
            s.pop()
        S[i] = i + 1 if len(s) == 0 else (i - s[-1])
        s.append(i)


def printArray(S, num):
    for i in range(0, num):
        print(S[i], end = '\t')


price = [10, 4, 5, 90, 120, 80]
S = [0 for i in range(len(price))]
calculateSpan(price, S)
printArray(S, len(price))
