import sys

# 입력 받기
N1, N2 = map(int, sys.stdin.readline().split())
N1_list = list(sys.stdin.readline().strip())  
N2_list = list(sys.stdin.readline().strip())  
T = int(sys.stdin.readline().strip())

# 첫 번째 그룹은 왼쪽 → 오른쪽, 두 번째 그룹은 오른쪽 → 왼쪽이므로 뒤집기
ants = list(reversed(N1_list)) + N2_list  # CBADEF 형태로 저장

groups = [1] * N1 + [2] * N2  # 개미 그룹 구분 - [1,1,1,2,2,2] 형태

for _ in range(T):  # T초 동안 반복

    i = 0

    while i < len(ants) - 1:  # 리스트의 끝까지 탐색

        if groups[i] == 1 and groups[i + 1] == 2:  # 앞 개미가 1번 그룹(→)이고, 뒤 개미가 2번 그룹(←)이면 점프!
            ants[i], ants[i + 1] = ants[i + 1], ants[i]  # 위치 변경 (점프)
            groups[i], groups[i + 1] = groups[i + 1], groups[i]  # 그룹도 변경
            i += 1  # 점프했으니 한 칸 건너뛰기
            
        i += 1  # 다음 개미로 이동

print("".join(ants))