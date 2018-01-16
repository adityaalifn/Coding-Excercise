def solution(A=[]):
    left = 0
    right = sum(A)
    result = float("Inf")
    for angka in A[:-1]:
        left += angka
        right -= angka
        result = min(result, abs(left - right))
    return result


print(solution([3, 1, 2, 4, 3]))
