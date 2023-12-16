def solution(S, P, Q):
    dict_ = {"A": [0], "C": [0], "G": [0], "T": [0]}
    for nucl in S:
        for type_, sums in dict_.items():
            if nucl == type_:
                sums.append(sums[-1] + 1)
            else:
                sums.append(sums[-1])
    queries = []
    for p, q in zip(P, Q):
        for i, type_ in enumerate("ACGT"):
            if dict_[type_][q + 1] > dict_[type_][p]:
                queries.append(i + 1)
                break
    return queries
