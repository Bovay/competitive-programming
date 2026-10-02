import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop

def main() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data) # data iterator (to keep track of input)

    n = int(next(it)) # size of array
    m = int(next(it)) # number of operations
    k = int(next(it)) # number of queries
    arr = [int(next(it)) for _ in range(n)]
    out = []

    ops = [] # holds the operations

    diffsum = [0] * (m + 2) # holds how many times each diff op is applied
    diffarr = [0] * (n + 2) # holds the actual diff values

    for i in range(m):
        l, r, d = int(next(it)), int(next(it)), int(next(it))
        ops.append((l, r, d))


    for i in range(1, k+1):
        l, r = int(next(it)), int(next(it))
        diffsum[l] += 1
        diffsum[r + 1] -= 1

    prefixsum = [0] * (m + 2)
    for i in range(1, m + 2):
        prefixsum[i] = prefixsum[i - 1] + diffsum[i] # now holds how many times each element is to be modified

    for i in range(1, m+1):
        l, r, d = ops[i-1]
        diffarr[l] += d * prefixsum[i]
        diffarr[r + 1] -= d * prefixsum[i]

    prefixarr = [0] * (n + 2)
    for i in range(1, n + 2):
        prefixarr[i] = prefixarr[i - 1] + diffarr[i] # now holds the actual diff values

    for i in range(n):
        out.append(arr[i] + prefixarr[i + 1])

    sys.stdout.write(" ".join(map(str, out)))


main()