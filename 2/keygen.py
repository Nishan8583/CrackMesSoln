import sys
def reverse(val,index):
        s = ""
        for i in range(0,4):
                s = s + val[index]
                index = index - 1
        print(s)
        return s


def key_gen(username):
    if len(username) < 5:
        print("Username not long enough, give atleast 5 length")
    count = len(username) - 3
    int_values = ""
    val = 1315632316
    total = 0
    value = ""
    end = 3
    while count != 0:
        value = reverse(username,end)
        print(value)
        int_values = "".join("{:02x}".format(ord(c)) for c in value)
        print(int_values)
        total = int(int_values,16)
        print(hex(total))
        val = val ^ total
        print(hex(val))
        count = count - 1
        end = end + 1
        int_values = ""
    print("FinalKey: FIT-{}".format(val))
key_gen(sys.argv[1])
