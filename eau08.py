import sys

if len(sys.argv) != 2 :
    print("error")
    exit()
elif sys.argv[1].isnumeric():
    print("true")
else:
    print("false")