def solution(A=[]):
    A.sort()
    if A == [i for i in range(1,len(A)+1)]:
        return 1
    return 0
    


print(solution([4,1,3,2]))
