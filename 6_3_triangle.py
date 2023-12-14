def solution(A):
    sorted_ = sorted(A)
    for i in range(len(sorted_) - 2):
        if sorted_[i] + sorted_[i + 1] > sorted_[i + 2]:
            return 1
    return 0
