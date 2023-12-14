def solution(A):
    to_east = 0
    passes = 0
    for number in A:
        if number == 0:
            to_east += 1
        else:
            passes += to_east
            if passes > 1000000000:
                return -1
    return passes
