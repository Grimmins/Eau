import sys
def checkString(index0, ch0, ch1, index1):
        if index1 == len(ch1):
            return True
        elif index0 >= len(ch0) or ch0[index0] != ch1[index1]:
            return False
        else:
            index1 += 1
            index0 += 1
            return checkString(index0,ch0,ch1,index1)

def checkTest(ch0, ch1):
    if ch1[0] not in ch0:
        return False
    for i in range(len(ch0)):
        if ch0[i] == ch1[0]:
            if checkString(i,ch0,ch1,0):
                return True
    return False

if len(sys.argv) != 3:
    print("error")
    exit()
else:
    print(checkTest(sys.argv[1],sys.argv[2]))