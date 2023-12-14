def solution(N):
    string = bin(N)[2:]
    gap_length = 0
    last_start = 0
    for i in range(1, len(string)):
        if string[i] == "1":
            gap_length = max(result, i - last_start - 1)
            last_start = i
    return gap_length
