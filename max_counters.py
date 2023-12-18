def solution(N, A):
    maxed_to = 0
    increase_dict = {}
    for number in A:
        if number == N + 1:
            maxed_to += max(increase_dict.values() or [0])
            increase_dict = {}
        else:
            increase_dict[n] = increase_dict.get(number, 0) + 1
    return [maxed_to + increase_dict.get(n + 1, 0) for number in range(N)]
