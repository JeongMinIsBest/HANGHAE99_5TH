words = [input() for _ in range(5)]

max_len = max(len(word) for word in words)

result = []
for col in range(max_len):
    for row in range(5):  # 5개의 행 반복
        if col < len(words[row]):  # 현재 열에 글자가 존재하면
            result.append(words[row][col])  # 해당 글자를 결과 리스트에 추가

# 출력
print(''.join(result))
