import sys
import heapq

N, M, K = map(int, sys.stdin.readline().split())
task = []

# 최대 힙을 만들기 위해 음수로 변환하여 저장
for _ in range(N):
    D = int(sys.stdin.readline().strip())
    heapq.heappush(tasks, -D)  # 최대 힙처럼 사용하기 위해 음수로 삽입

days = 0  # 일을 끝내는 데 걸리는 총 일수
satisfaction = 0  # 전날 만족도
satisfaction_list = []  # 각 날의 만족도를 저장할 리스트

# 모든 일이 끝날 때까지 반복
while tasks:
    days += 1
    P = -heapq.heappop(tasks)  # 가장 중요한 일 선택 (음수 → 양수 변환)
    satisfaction = (satisfaction // 2) + P  # 오늘의 만족감 계산
    satisfaction_list.append(satisfaction)  # 만족감을 리스트에 추가

    P -= M  # 중요도 감소
    if P > K:
        heapq.heappush(tasks, -P)  # 다시 힙에 추가 (음수 변환)

# 결과 출력
print(days)
print("\n".join(map(str, satisfaction_list)))