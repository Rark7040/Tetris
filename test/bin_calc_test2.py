b = 0b100001001010

while b != 0b1:
    dump = b & 0b1
    # print(True if dump == 0b1 else False)

    b = b >> 1
    print(bin(b))
