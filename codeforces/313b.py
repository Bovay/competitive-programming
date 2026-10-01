import sys
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop

def main() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    s = next(it).decode()
    m = int(next(it))
    n = len(s)
    out = []

    pre = [0] * (n + 1)
    for i in range(1, n):
        pre[i] = pre[i - 1] + (s[i - 1] == s[i])

    for i in range(m):
        l, r = int(next(it)), int(next(it))
        out.append(pre[r - 1] - pre[l - 1])


    sys.stdout.write("\n".join(map(str, out)))


main()