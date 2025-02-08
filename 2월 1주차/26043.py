import sys
from collections import deque

n = int(sys.stdin.readline().strip())

queue = deque() # FIFO 대기열

A = [] # 좋아하는 메뉴를 먹은 학생
B = [] # 안 좋아하는 메뉴를 먹은 학생
C = [] # 식사를 못 한 학생

for _ in range(n):
    info = list(map(int, sys.stdin.readline().split()))

    if info[0] == 1:
        # 1: 학생이 줄을 섰을 때
        a, b = info[1], info[2]
        queue.append((a, b))

    elif info[0] == 2:
        # 2: 메뉴가 제공될 때
        b = info[1]
        student, favorite_menu = queue.popleft()

        if favorite_menu == b:
            A.append(student)
        else:
            B.append(student)

while queue:
    C.append(queue.popleft()[0])

print(" ".join(map(str, sorted(A))) if A else "None")
print(" ".join(map(str, sorted(B))) if B else "None")
print(" ".join(map(str, sorted(C))) if C else "None")