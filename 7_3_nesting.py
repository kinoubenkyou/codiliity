def solution(S):
    if not S:
        return 1
    stack = []
    for char in S:
        if char == "(":
            stack.append(char)
        if char == ")":
            if not stack or stack[-1] != "(":
                return 0
            else:
                stack.pop()
    if stack:
        return 0
    return 1
