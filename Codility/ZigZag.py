class Tree(object):
    x = 0
    l = None
    r = None


def solution(T):
    # write your code in Python 3.6
    if T == None:
        return 0
    
    return max(getZigZag(T, True, 0), getZigZag(T, False, 0))


def getZigZag(now, right, counter):
    if now == None:
        return counter

    if right == True:
        if now.r == None:
            counter += 1
        getZigZag(now.r, not right, counter)
    else:
        if now.l == None:
            counter += 1
        getZigZag(now.l, not right, counter)

    return counter


print(solution((5, (3, (20, (6, None, None), None), None), (10,
                                                            (1, None, None), (15, (30, None, (9, None, None)), (8, None, None))))))
