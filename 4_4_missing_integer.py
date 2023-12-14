def solution(A):
    set_ = set([n for n in A if n > 0])
    result = 1
    while result in set_:
        result += 1
    return result
