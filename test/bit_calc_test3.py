b = 0b110011
cal = 0b1 << 4
print(bin((b & ~cal)))
print(bin((b & cal) == cal))