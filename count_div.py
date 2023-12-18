def solution(A, B, K):
    divs_after_a_to_b = B // K - A // K
    if A % K == 0:
        return divs_after_a_to_b + 1
    else:
        return divs_after_a_to_b
