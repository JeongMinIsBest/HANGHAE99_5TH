import heapq
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0]) # 방문 횟수

max_heap = [] # 최대 힙을 사용

index = 1 # 현재 읽을 데이터의 위치

for _ in range(n):
    a = int(data[index])
    index += 1

    if a > 0:
        for _ in range(a):
            gift_value = int(data[index])
            index += 1
            heapq.heappush(max_heap, -gift_value)

    else:
        if not max_heap:
            print(-1)
        else :
            print(-heapq.heappop(max_heap))