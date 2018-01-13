def solution(A=[]):
    # pairs = []
    # for i in A:
    #     if i not in pairs:
    #         pairs.append(i)
    #     else:
    #         pairs.remove(i)
    # if len(pairs) == 0:
    #     return 0
    # else:
    #     return pairs[0]
    sol = 0
    for number in A:
        sol ^= number
        print(sol)
 
    return sol


print(solution([9, 3, 9, 3, 9, 7, 9]))
