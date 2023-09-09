import sys

def between(a,b):
    nbX = []
    if a < b:
        for i in range(a,b):
            nbX.append(i)
        return nbX
    else:
        between(b,a)


if len(sys.argv) != 3 or not sys.argv[1].isnumeric() or not sys.argv[2].isnumeric():
    print("error")
    exit()
else:
    [print(i, end=" ") for i in between(int(sys.argv[1]), int(sys.argv[2]))]
    print("\n")