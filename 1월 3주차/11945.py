N, M = map(int, input().split()) 
fish = []

for _ in range(N):
    fish_in = input()
    fish.append(fish_in[::-1]) 

print("\n".join(fish))