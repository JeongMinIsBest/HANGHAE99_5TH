fruit_count = {
    "STRAWBERRY" : 0,
    "BANANA" : 0,
    "LIME" : 0,
    "PLUM" : 0
}

N = int(input())

for _ in range(N) :
    S, X = input.split()
    X = int(X)
    fruit_count[S] += X

if 5 in fruit_count.values():
    print("YES")
else:
    print("NO")
