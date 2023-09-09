import sys

def ascii_sort(Args):
    for i in range(len(Args)):
        min_index = i
        for j in range(i + 1, len(Args)):
            if Args[j] < Args[min_index]:
                min_index = j
        Args[i], Args[min_index] = Args[min_index], Args[i]
    return Args

if len(sys.argv) < 2:
    print("error")
    exit()

Args = sys.argv[1:]
[print(i, end=" ") for i in ascii_sort(Args)]
print('\n')