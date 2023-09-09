import sys


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

if len(sys.argv) != 2 or not sys.argv[1].isnumeric():
    print(-1)
else:
    print(fib(int(sys.argv[1])))

