import sys

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
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
    [print(i, end=" ") for i in selection_sort(recupArgs())]
    print('\n')

