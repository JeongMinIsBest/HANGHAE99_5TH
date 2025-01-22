L = int(input())
String = input()

r= 31
M = 1234567891

hash_value = 0

for i in range(L):
    char_value = ord(String[i]) - ord('a') + 1
    hash_value += char_value * (r ** i) % M

hash_value %= M

print(hash_value)
