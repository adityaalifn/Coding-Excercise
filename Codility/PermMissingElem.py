def solution(A=[]):
    A_len = len(A) + 1
    val = (A_len * (A_len + 1)) / 2
    return int(val - sum(A))

print(solution([2,3,1,5]))