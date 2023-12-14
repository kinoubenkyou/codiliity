def solution(A):
    set_ = set([n for n in A if n > 0])
    missing = 1
    while missing in set_:
        missing += 1
    return missing
