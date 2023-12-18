def solution(A):
    set_ = set()
    for number in A:
        if number in set_:
            set_.remove(number)
        else:
            set_.add(number)
    return set_.pop()
