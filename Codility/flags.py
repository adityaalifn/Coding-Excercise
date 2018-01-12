def solution(A=[]):
    peaks = []

    for i in range(1, len(A) - 1):
        if ((A[i] > A[i - 1]) and (A[i] > A[i + 1])):
            peaks.append(i)
            i += 1
    
    if len(peaks == 0):
        return 0
    

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]
A[0] = 1
A[1] = 5
A[2] = 3
A[3] = 4
A[4] = 3
A[5] = 4
A[6] = 1
A[7] = 2
A[8] = 3
A[9] = 4
A[10] = 6
A[11] = 2

print(solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]))
print(solution(A))
