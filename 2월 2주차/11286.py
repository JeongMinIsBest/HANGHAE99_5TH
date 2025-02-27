import sys
import heapq

N = int(sys.stdin.readline().strip())

heap = []

for _ in range(N):
    a = int(sys.stdin.readline().strip())
    if a != 0:
        heapq.heappush(heap, (abs(a), a))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)