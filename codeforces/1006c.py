import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop

def main() -> None:
    data = sys.stdin.buffer.read().split()
    out = []
    it = iter(data) # data iterator (to keep track of input)

    n = int(next(it)) # size of array

    arr = [int(next(it)) for _ in range(n)] # array of integers

    l = 0 # left pointer
    r = n - 1 # right pointer

    leftSum = arr[l]
    rightSum = arr[r]

    largestSum = 0

    while l < r: # bug occurred here since it was l <= r
        if leftSum == rightSum: # bug occurred here since this flag was at the end instead of the start
            largestSum = leftSum
    
        if leftSum <= rightSum:
            l += 1
            if l >= r:
                break
            leftSum += arr[l]
        else:
            r -= 1
            if l >= r:
                break
            rightSum += arr[r]

    out.append(largestSum)
   
    sys.stdout.write(" ".join(map(str, out)))


main()