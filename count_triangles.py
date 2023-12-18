def solution(A):
    sorted_ = sorted(A)
    count = 0
    for first in range(len(A) - 2):
        second = first + 1
        third = first + 2
        while second < len(A) - 1:
            if third < len(A) and sorted_[first] + sorted_[second] > sorted_[third]:
                third += 1
            else:
                count += third - second - 1
                second += 1
    return count
