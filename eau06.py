import string
import sys

def maj(ch0):
    ch1 = ""
    j = 0
    for i in range(len(ch0)):
        if ch0[i] not in string.ascii_letters:
            ch1 += ch0[i]
            continue
        else:
            if j%2 == 0:
                ch1 += ch0[i].upper()
                j += 1
            else:
                ch1 += ch0[i]
                j += 1
    return ch1



if len(sys.argv) != 2 or sys.argv[1].isnumeric():
    print("error")
    exit()
else:
    print(maj(sys.argv[1]))