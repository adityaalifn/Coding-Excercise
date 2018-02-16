
def maze1(S):
    kiri = True
    for baris in range(S):
        if (baris % 2 == 0):
            if kiri == True:
                for i in range(S):
                    if i == 1:
                        print(" ", end="")
                    else:
                        print("@", end="")
                print("")
                kiri = False
            else:
                for j in range(S):
                    # print(S)
                    # print(j)
                    if j == S-2:
                        print(" ",end="")
                    else:
                        print("@", end="")
                print("")
                kiri = True
        else:
            for i in range(S):
                if i == 0:
                    print("@",end="")
                elif i == S-1:
                     print("@")
                    #  print("A")
                else:
                    print(" ",end="")

maze1(15)