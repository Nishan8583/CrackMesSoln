def keygen(name):
    length = str(len(name))
    firstChar = str(ord(name[0]))
    s = str(getSum(name))
    print(length+str(0x6e)+firstChar+s)

def getSum(name):
    sums = 0
    for i in name:
        sums = sums + ord(i)
    return sums
keygen("Solta")
