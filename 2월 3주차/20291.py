import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip()) 
file_count = defaultdict(int) 

for _ in range(N):
    file_name, extension = sys.stdin.readline().strip().split(".")  # 파일명과 확장자 분리
    file_count[extension] += 1  # 확장자 개수 증가

# 확장자 사전순 정렬 후 출력
for ext in sorted(file_count.keys()):
    print(ext, file_count[ext])

