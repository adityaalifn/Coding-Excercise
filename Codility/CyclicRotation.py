def solution(A, K):
    A_copy = A.copy()
    A_len = len(A)
    if A_len <= 1:
        return A
    K = K % A_len
    return A[-K:] + A[:-K]

A = [1]
K = 3

print(solution([1,2,3], 613))