def solution(N):
    power = 1
    highest = 0
    while 2 ** power == N or 2 * (2 ** power) <= N:
        if N % (2 ** power) == 0:
            highest = power
        power += 1
    return highest
