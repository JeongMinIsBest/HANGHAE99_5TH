import sys

while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".":
        break

    stack = []
    balanced = True
    brackets = {')': '(', ']': '['}

    for char in sentence:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')' or char == ']':
            if not stack or stack[-1] != brackets[char]:
                balanced = False
                break
            stack.pop()

    if balanced and not stack:
        print("yes")
    else:
        print("no")