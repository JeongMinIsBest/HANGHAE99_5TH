from collections import defaultdict

N, M = map(int, input().split())

student_counts = defaultdict(int)

for _ in range(N):
    K_i = int(input())
    student_ids = list(map(int, input().split()))

    for student_id in student_ids:
        student_counts[student_id] += 1

result = sum(1 for count in student_counts.values() if count >= M)

print(result)