b = 0b10001001010

while b != 0b0:
    dump = b & 0b1
    print(bin(b))
    print(True if dump == 0b1 else False)

    b = b >> 1
