def solution(A):
    node = A[0]
    count = 1
    while node > -1:
        count += 1
        node = A[node]
    return count
