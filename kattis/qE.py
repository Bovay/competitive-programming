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

    for i in range (n):
        k = int(next(it))
        arr = [["."] * k for _ in range(k)]

        arr[0][1] = "C"
        arr[1][0] = "C"

        for row in arr:
            out.append("".join(row))

    sys.stdout.write("\n".join(map(str, out)))


main()