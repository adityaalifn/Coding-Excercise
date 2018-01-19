def solution(X, A):
    sol = [i for i in range(1,X+1)]
    now = []
    for i in range(len(A)):
        if A[i] not in now:
            now.append(A[i])
        if sorted(now) == sol:
            return i
    return -1


print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
