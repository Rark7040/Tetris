from soft.BitBlock import BitBlock

block = BitBlock()
block.set(0b1100)
block.set(0b1100)
block.set(0b1100)

for b in block.get_all():
    print(bin(b))

print("\n\n\n")

for b in block.rotate_to_left():
    print(bin(b))

print("\n\n\n")


new_block = BitBlock()
for nb in block.rotate_to_left():
    new_block.set(nb)

for nb in new_block.rotate_to_left():
    print(bin(nb))

print("\n\n\n")

new_block2 = BitBlock()
for nb in new_block.rotate_to_left():
    new_block2.set(nb)

for nb in new_block2.rotate_to_left():
    print(bin(nb))