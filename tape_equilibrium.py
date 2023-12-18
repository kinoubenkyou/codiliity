def solution(A):
    left_sum = A[0]
    right_sum = sum(A[1:])
    difference = abs(left_sum - right_sum)
    for i in range(2, len(A)):
        left_sum += A[i - 1]
        right_sum -= A[i - 1]
        difference = min(difference, abs(left_sum - right_sum))
    return difference
