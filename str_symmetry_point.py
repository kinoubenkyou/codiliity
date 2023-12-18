def solution(S):
    if not S or len(S) % 2 == 0:
        return -1
    i = 0
    while i < len(S) // 2:
        if S[i] != S[-i - 1]:
            return -1
        i += 1
    return i
