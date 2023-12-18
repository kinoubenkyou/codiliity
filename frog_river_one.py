def solution(X, A):
    leaves_needed = set(range(1, X + 1))
    for i in range(len(A)):
        leaves_needed.discard(A[i])
        if not leaves_needed:
            return i
    return -1
