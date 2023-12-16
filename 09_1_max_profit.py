def solution(A):
    differences = []
    for i in range(len(A) - 1):
        differences.append(A[i + 1] - A[i])
    return max_sum_of_slice(differences)

def max_sum_of_slice(list_):
    max_ending = max_slice = 0
    for element in list_:
        max_ending = max(0, max_ending + element)
        max_slice = max(max_slice, max_ending)
    return max_slice
