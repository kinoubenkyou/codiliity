def solution(N, A):
    maxed_to = 0
    increase_dict = {}
    for n in A:
        if n == N + 1:
            maxed_to += max(increase_dict.values() or [0])
            increase_dict = {}
        else:
            increase_dict[n] = increase_dict.get(n, 0) + 1
    return [maxed_to + increase_dict.get(n + 1, 0) for n in range(N)]
