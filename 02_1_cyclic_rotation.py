def solution(A, K):
    if not A:
        return A
    rotates = K % len(A)
    return A[-rotates:] + A[:-rotates]
