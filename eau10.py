import sys

def searchIndex(L,element):
    if element not in L:
        return -1
    return L.index(element)

def recupArgs():
    return [sys.argv[i] for i in range(1,len(sys.argv)-1)]

if len(sys.argv) == 1:
    print("error")
    exit()
print(searchIndex(recupArgs(),sys.argv[-1]))
