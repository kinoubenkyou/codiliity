def solution(A, B):
    stack = []
    for size, direction in zip(A, B):
        while True:
            if not stack:
                stack.append([size, direction])
                break
            last_fish = stack[-1]
            if last_fish[1] == direction or last_fish[1] == 0:
                stack.append([size, direction])
                break
            elif last_fish[0] > size:
                break
            else:
                stack.pop()
    return len(stack)
