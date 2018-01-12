def soultion(N):
    try:
        N = int(N)
        N = str(bin(N))[2:]
    except Exception as e:
        return 0

    max_hit = 0
    hit = 0

    for i in N:
        if i == "0":
            hit += 1

        if i == "1":
            if hit > max_hit:
                max_hit = hit
            hit = 0
    return max_hit


print(soultion(input()))
