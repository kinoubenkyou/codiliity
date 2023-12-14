def solution(X, Y, D):
    jumps_before_pass = (Y - X) // D
    if (Y - X) % D > 0:
        return jumps_before_pass + 1
    else:
        return jumps_before_pass
