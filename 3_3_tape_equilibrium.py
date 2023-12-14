def solution(A):
    left_sum = A[0]
    right_sum = sum(A[1:])
    result = abs(left_sum - right_sum)
    for i in range(2, len(A)):
        left_sum += A[i - 1]
        right_sum -= A[i - 1]
        result = min(result, abs(left_sum - right_sum))
    return result
