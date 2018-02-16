def solution(N):
    counter = 0
    for i in range(1,N+1):
        if N % i == 0:
            counter += 1
    return counter

print(solution(24))