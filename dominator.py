def solution(A):
    size = 0
    candidate = None
    for number in A: 
        if size == 0:
            size += 1
            candidate = number
        elif number == candidate:
            size += 1
        else:
            size -= 1
    if size == 0:
        return -1
    count = 0
    for i, number in enumerate(A):
        if number == candidate:
            count += 1
            if count > len(A) / 2:
                return i
    return -1
