def solution(N):
    string = bin(N)[2:]
    result = 0
    last_start = 0
    for i in range(1, len(string)):
        if string[i] == "1":
            result = max(result, i - last_start - 1)
            last_start = i
    return result
