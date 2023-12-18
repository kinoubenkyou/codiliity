def solution(K, A):
    sum_length = 0
    count = 0
    for i, length in enumerate(A):
        sum_length += length
        if sum_length >= K:
            count += 1
            sum_length = 0
    return count
