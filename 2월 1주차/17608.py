import sys

N = int(sys.stdin.readline().strip())  
heights = [int(sys.stdin.readline().strip()) for _ in range(N)]  

count = 1  
max_height = heights[-1] 

for i in range(N - 2, -1, -1):  
    if heights[i] > max_height:
        count += 1
        max_height = heights[i] 

print(count)