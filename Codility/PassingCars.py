def solution(A):
    passing = 0
    count = 0
    for i in A:
        if i == 1:
            passing += count
            if passing > 1000000000:
                return -1
        else:
            count += 1
    return passing

print(solution())