def solution(A):
    if len(A) == 1:
        return A[0]
    max_ending = max_slice = A[0]
    for element in A[1:]:
        max_ending = max(element, max_ending + element)
        max_slice = max(max_slice, max_ending)
    return max_slice
