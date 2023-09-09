import sys

def isPrime(n):
    if n == 1: return False
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            return False
    return True


def nextPrime(n):
    test = False
    while not test:
        if isPrime(n+1):
            return n+1
        else:
            n += 1

if len(sys.argv) != 2 or not sys.argv[1].isnumeric():
    print(-1)
else:
    print(nextPrime(int(sys.argv[1])))