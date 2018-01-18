def solution(A=[]):
    A = sorted(A)
    if A == range(1, len(A) + 1):
        return 1
    return 0


print(solution([1, 2, 3, 4, 6]))
