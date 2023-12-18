def solution(A):
    set_ = set()
    non_uniques = set()
    for number in A:
        if number in set_:
            non_uniques.add(number)
        set_.add(number)
    uniques = set_ - non_uniques
    for number in A:
        if number in uniques:
            return number
    return -1
