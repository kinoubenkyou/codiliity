def solution(N):
    if N == 1:
        return 1
    i = 2
    factor_count = 1
    while i * i < N:
        if N % i == 0:
            factor_count += 1
        i += 1
    return factor_count * 2 + int(i * i == N)
