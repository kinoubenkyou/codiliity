def solution(A):
    if not A:
        return 1
    max_ = max(A)
    set_ = set(A)
    for number in range(1, max_ + 1):
        if number not in set_:
            return number
    return max_ + 1
