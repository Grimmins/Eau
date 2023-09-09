

def retireDoublons(L):
    return [i for i in L if i[1] != i[0] and i[0] != i[2] and i[1] != i[2]]

def growElements(L):
    return [i for i in L if int(i[0]) < int(i[1]) and int(i[1]) < int(i[2])]


nbX = [ str(i).zfill(3) for i in range(1000) ]
[print(i + ", ", end="") for i in retireDoublons(growElements(nbX))]