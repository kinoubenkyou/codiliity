def solution(A):
    lefts = []
    rights = []
    for center, radius in enumerate(A):
        lefts.append(center - radius)
        rights.append(center + radius)
    lefts.sort()
    rights.sort()
    left_i = 0
    intersects = 0
    for right_i, right in enumerate(rights):
        while (
            left_i < len(lefts)  # when all discs are counted, cannot check current non-existing disc
            and lefts[left_i] <= right
        ):
            left_i += 1
        intersects += (
            left_i
            - 1  # the current disc
            - right_i  # discs intesected in previous counts or not intersects
        )
        if intersects > 10000000:
            return -1
    return intersects
