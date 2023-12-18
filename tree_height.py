def solution(T):
    memo = {"max_height": 0}
    traverse(T, 0, memo)
    return memo["max_height"]

def traverse(node, height, memo):
    if not node.l and not node.r:
        memo["max_height"] = max(memo["max_height"], height)
    if node.l:
        traverse(node.l, height + 1, memo)
    if node.r:
        traverse(node.r, height + 1, memo)
