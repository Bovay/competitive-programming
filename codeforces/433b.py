import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop

def main() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data) # data iterator (to keep track of input)
    arrlen = int(next(it)) # how many numbers there is
    arr = []
    for _ in range(arrlen):
        arr.append(int(next(it)))

    prefixunsorted = [0] * (arrlen + 1)
    prefixsorted = [0] * (arrlen + 1)

    temp = sorted(arr)

    for i in range(1, arrlen + 1):
        prefixunsorted[i] = prefixunsorted[i - 1] + int(arr[i - 1])
        prefixsorted[i] = prefixsorted[i - 1] + int(temp[i - 1])

    m = int(next(it))
    out = []
    for i in range(m):
        j = int(next(it)) # type of query
        l, r = int(next(it)), int(next(it)) # range of query
        if j == 2:
            out.append(prefixsorted[r] - prefixsorted[l - 1])
        else:
            out.append(prefixunsorted[r] - prefixunsorted[l - 1])
    

    sys.stdout.write("\n".join(map(str, out)))


main()