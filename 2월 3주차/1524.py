import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):

    N, M = map(int, sys.stdin.readline().split())
    SJ = map(int, sys.stdin.readline().split())
    SB = map(int, sys.stdin.readline().split())

    SJ.sort()
    SB.sort()

    # 투 포인터 방식으로 전투 진행
    i, j = 0, 0

    while i < N and j < M:

        if SJ[i] < SB[j]:
            i += 1 # 세준이의 병사 제거

        else:
            j += 1 # 세비의 병사 제거 (둘이 같으면 세비가 제거됨)

    if i < N: # 세준이 병사가 남아있음
        print('S')

    elif j < M: # 세비의 병사가 남아있음
        print('B')
        
    else:
        print('C') # 둘다 아님

    