def solution(A=[]):
    # n = len(A)
    # count = [0] * (n+1)
    # for i in range(n):
    #     count[A[i]] += 1
    # return A.pop(count.index(min(count)))
    A.sort()
    min = 1
    for i in A:
        if i == min:
            min+=1
    return min


print(solution([1, 3, 6, 4, 1, 2]))
print(solution([1, 2, 3]))
print(solution([-1, 2, 3]))
