def solution(S):
    pairs = {")": "(", "]": "[", "}": "{"}
    if not S:
        return 1
    stack = []
    for char in S:
        if char in pairs.values():
            stack.append(char)
        if char in pairs.keys():
            if not stack or stack[-1] != pairs[char]:
                return 0
            else:
                stack.pop()
    return 1
