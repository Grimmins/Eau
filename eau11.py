import sys

def absoluteDiffMin(nb):
    minAbs = sys.maxsize
    for i in range(len(nb)):
        nbX = [nb[j] for j in range(len(nb)) if j != i]
        for k in nbX:
            minAbs = min(minAbs, abs(nb[i]-k))

    return minAbs

def recupArgs():
    return [int(sys.argv[i]) for i in range(1,len(sys.argv))]

def checkArgs(index):
    if index == len(sys.argv) - 1:
        return sys.argv[index].lstrip("-").isnumeric()
    return sys.argv[index].lstrip("-").isnumeric() and checkArgs(index+1)

if len(sys.argv) < 3 or not checkArgs(1):
    print("error")
    exit()
else:
    print(absoluteDiffMin(recupArgs()))

