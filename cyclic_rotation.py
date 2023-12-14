def solution(A, K):
    if not A:
        return A
    rotate_times = K % len(A)
    return A[-rotate_times:] + A[:-rotate_times]
