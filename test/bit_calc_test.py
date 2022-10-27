b: int = 0b1011
b2: int = 0b1001

print(bin(b & ~b2))
print((b & 0b1000) == 0b1000)
