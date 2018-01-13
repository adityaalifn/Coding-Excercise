def solution(A, K):
    A_copy = A.copy()
    A_len = len(A)
    for i in range(A_len):
        A[i+K-A_len] = A_copy[i]
    return A

A = [3, 8, 9, 7, 6]
K = 3

print(solution(A,K))