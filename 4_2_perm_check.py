def solution(A):
    set_ = set()
    for n in A:
        if n in set_:
            return 0
        else:
            set_.add(n)
    for n in range(1, max(A) + 1):
        if n not in set_:
            return 0
    return 1
