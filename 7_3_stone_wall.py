def solution(H):
    stack = []
    blocks = 0
    for height in H:
        while True:
            if not stack:
                stack.append(height)
                break
            elif stack[-1] == height:
                break
            elif stack[-1] < height:
                stack.append(height)
                break
            else:
                stack.pop()
                blocks += 1
    return blocks + len(stack)
