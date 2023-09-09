import sys

def recupListArgs():
    return [sys.argv[i] for i in range(1, len(sys.argv))]

if len(sys.argv) == 1:
    print("error")
    exit()
[print(recupListArgs()[i]) for i in range(len(recupListArgs())-1,-1,-1)]
