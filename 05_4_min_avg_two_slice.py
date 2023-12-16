def solution(A):
    minimal = (A[0] + A[1]) / 2
    start = 0
    for i in range(2, len(A)):
        average_three = (A[i - 2] + A[i - 1] + A[i]) / 3
        if average_three < minimal:
            minimal = average_three
            start = i - 2
        average_two = (A[i - 1] + A[i]) / 2
        if average_two < minimal:
            minimal = average_two
            start = i - 1
    return start
