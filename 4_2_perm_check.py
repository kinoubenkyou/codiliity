def solution(A):
    set_ = set()
    for number in A:
        if number in set_:
            return 0
        else:
            set_.add(number)
    for number in range(1, max(A) + 1):
        if number not in set_:
            return 0
    return 1
