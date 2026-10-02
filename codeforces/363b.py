from calendar import c
from locale import currency
import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop

def main() -> None:
    data = sys.stdin.buffer.read().split()
    out = []
    it = iter(data) # data iterator (to keep track of input)

    n = int(next(it))
    k = int(next(it))

    arr = [int(next(it)) for _ in range(n)]
    minindex = 1

    sum_ = sum(arr[0:k])
    minsum_ = sum_

    for i in range(1, n - k + 1):
        sum_ = sum_ - arr[i-1] + arr[i+k-1]
        if sum_ < minsum_:
            minindex = i+1
            minsum_ = sum_

    out.append(minindex)
            
    sys.stdout.write(" ".join(map(str, out)))


main()