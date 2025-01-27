import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dict = {}

for _ in range(N):
    song = input().split()
    sound = ''.join(song[2:5])

    if sound in dic_song:
        dic_song[sound] = '?'
    else :
        dic_song[sound] = '!'

for _ in range(m):
    sound = ''.join(input().split())

    if sound in dic_song:
        print(dic_song[sound])
    else:
        print('!')