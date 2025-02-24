import sys

N = int(input())
coords = list(map(int, sys.stdin.readline().split()))

# 중복을 제거한 후 정렬
sorted_unique = sorted(set(coords))

# 각 좌표의 압축된 값을 매핑
coord_map = {value: index for index, value in enumerate(sorted_unique)}

# 원래 배열을 압축된 값으로 변환
compressed_coords = [coord_map[x] for x in coords]

# 결과 출력
print(" ".join(map(str, compressed_coords)))