def solution(N):
    number = side = 1
    while number * number <= N:
        if N % number == 0:
            side = number
        number += 1
    return 2 * (side + N // side)
