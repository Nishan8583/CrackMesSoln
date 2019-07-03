def keygen(s):
    total = 0
    s = s.upper()
    for i in s:
        i = ord(i)
        i = i * 0x1749
        i = i - 1
        total = total + i
    print("SnD-{}".format(total))
keygen("iamhero")
