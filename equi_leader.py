def solution(A):
    size = 0
    leader = None
    for number in A: 
        if size == 0:
            size += 1
            leader = number
        elif number == leader:
            size += 1
        else:
            size -= 1
    left_count = 0
    right_count = A.count(leader)
    equi_leader_count = 0
    for i in range(len(A) - 1):
        if A[i] == leader:
            left_count += 1
            right_count -= 1
        if left_count > (i + 1) / 2 and right_count > (len(A) - i - 1) / 2:
            equi_leader_count += 1
    return equi_leader_count
