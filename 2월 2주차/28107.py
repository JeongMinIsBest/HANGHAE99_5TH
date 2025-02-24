import sys
from collections import defaultdict

N, M = map(int, sys.stdin.readline().split())

# 초밥을 원하는 손님 목록을 저장할 딕셔너리
sushi_preferences = defaultdict(list)
eaten_sushi = [set() for _ in range(N)] # 각 손님이 먹은 초밥 저장
sushi_count = [0] * N # 각 손님이 먹은 초밥 개수

# N명의 손님이 각자 먹고 싶은 초밥 목록을 입력 받음
for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    k, favorites = data[0], data[1:]
    
    for sushi in favorites:
        sushi_preferences[sushi].append(i) # 해당 초밥을 원하는 손님 리스트에 추가

# 요리된 초밥을 입력 받음
sushi_list = list(map(int, sys.stdin.readline().split()))

# 초밥을 순서대로 처리
for sushi in sushi_list:

    if sushi in sushi_preferences: # 이 초밥을 원하는 손님이 있을 때만 확인

        for customer in sushi_preferences[sushi]: # 초밥을 원하는 손님목록 불러오기

            if sushi not in eaten_sushi[customer]: # 이미 먹지 않았다면
                sushi_count[customer] += 1 # 먹은 초밥 개수 증가
                eaten_sushi[customer].add(sushi) # 초밥 먹었다고 기록
                break # 가장 앞 순서의 손님이 먹었으므로 종료

print(" ". join(map(str, sushi_count)))