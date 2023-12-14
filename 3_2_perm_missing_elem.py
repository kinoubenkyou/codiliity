def solution(A):
    if not A:
        return 1
    max_ = max(A)
    if max_ == len(A):
        return max_ + 1
    return (set(range(1, max_ + 1)) - set(A)).pop()
