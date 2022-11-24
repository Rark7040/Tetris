from src.soft.BitBlock import BitBlock

block = BitBlock()
block.set(0b1100)
block.set(0b1111)
block.set(0b1100)

for b in block.get_all_bits():
    print(bin(b))

print("\n")

for b in block.rotate_to_left().get_cloning_bits():
    print(bin(b))

print("\n")

for b in block.rotate_to_left().rotate_to_left().get_cloning_bits():
    print(bin(b))

print("\n")

for b in block.rotate_to_left().rotate_to_left().rotate_to_left().get_cloning_bits():
    print(bin(b))

print("\n")

