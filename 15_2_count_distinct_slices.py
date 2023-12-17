def solution(M, A):
    start = 0
    end = 0
    unique_values = set()
    count = 0
    while start < len(A) and end < len(A):
        if A[end] in unique_values:
            unique_values.remove(A[start])
            start += 1
        else:
            count += end + 1 - start
            if count > 1_000_000_000:
                return 1_000_000_000
            unique_values.add(A[end])
            end += 1
    return count
