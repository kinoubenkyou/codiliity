def solution(A):
    set_ = set()
    for number in A:
        set_.add(abs(number))
    return len(set_)
