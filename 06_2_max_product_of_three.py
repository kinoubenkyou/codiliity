0def solution(A):
    possible_results = set()
    if 0 in A:
        possible_results.add(0)
    sorted_ = sorted(A)
    possible_results.add(sorted_[0] * sorted_[1] * sorted_[-1])
    possible_results.add(sorted_[-3] * sorted_[-2] * sorted_[-1])
    return max(possible_results)
