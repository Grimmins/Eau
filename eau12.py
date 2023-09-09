import sys

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def recupArgs():
    return [int(sys.argv[i]) for i in range(1,len(sys.argv))]

def checkArgs(index):
    if index == len(sys.argv) - 1:
        return sys.argv[index].lstrip("-").isnumeric()
    return sys.argv[index].lstrip("-").isnumeric() and checkArgs(index+1)


if len(sys.argv) == 1 or not checkArgs(1):
    print("error")
    exit()
else:
    [print(i, end=" ") for i in bubble_sort(recupArgs())]
    print('\n')

