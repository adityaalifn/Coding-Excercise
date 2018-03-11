# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, T):
    # write your code in Python 3.6
    if len(S) != len(T):
        return False
    
    set_angka = "0123456789"

    S_new = ""
    T_new = ""

    for i in S:
        if i in set_angka:
            S_new += "?" * int(i)
            continue
        S_new += i

    for i in T:
        if i in set_angka:
            T_new += "?" * int(i)
            continue
        T_new += i
    
    print(S_new, T_new)

    for i in range(len(S_new)):
        if S_new[i] != "?" and T_new[-1*(i+1)] != "?" and S_new[i] != T[-1*(i+1)]:
            return False

    return True

print(solution("ba1", "1Ad"))