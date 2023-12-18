def solution(A, B):
    if not A:
        return 0
    current_start = A[-1]
    count = 1
    for i in range(len(A) - 2, -1, -1):
        if B[i] < current_start:
            count += 1
            current_start = A[i]
        if A[i] > current_start:
            current_start = A[i]
    return count
