import sys

def maj(ch0):
    ch1 = ch0[0].upper()
    for i in range(1, len(ch0)):
        if ch0[i - 1] in [' ', '\n', '\t']:
            ch1 += ch0[i].upper()
        else:
            ch1 += ch0[i]
    return ch1

if len(sys.argv) != 2 or sys.argv[1].isnumeric():
    print("error")
    exit()
else:
    print(maj(sys.argv[1]))
