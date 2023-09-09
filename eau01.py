
def growElements(L):
    return [i for i in L if int(i[0]) < int(i[1])]

nbX = [[str(i).zfill(2),str(j).zfill(2)] for i in range(100) for j in range(100)]
[print(i[0] + " " + i[1] + ", ", end="") for i in growElements(nbX)]

