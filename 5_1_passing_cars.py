def solution(A):
    to_east = 0
    result = 0
    for n in A:
        if n == 0:
            to_east += 1
        else:
            result += to_east
            if result > 1000000000:
                return -1
    return result
