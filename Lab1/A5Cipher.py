def shift(register, feedback):
    xor = 0
    for bit in feedback:
        xor ^= (register >> bit) & 1
    return ((register << 1) & ((1 << len(bin(register)) - 2) - 1)) | xor

def majority(x, y, z):
    return (x & y) | (x & z) | (y & z)

def a5_1_keystream(x, y, z, n):
    keystream = []
    for _ in range(n):
        maj = majority((x >> 8) & 1, (y >> 10) & 1, (z >> 10) & 1)
        if ((x >> 8) & 1) == maj:
            x = shift(x, [13, 16, 17, 18])
        if ((y >> 10) & 1) == maj:
            y = shift(y, [20, 21])
        if ((z >> 10) & 1) == maj:
            z = shift(z, [7, 20, 21, 22])
        keystream.append(((x ^ y ^ z) & 1))
    return keystream

# Initial register values in decimal
X0 = 513365
Y0 = 3355443
Z0 = 7401712
n = 10

keystream = a5_1_keystream(X0, Y0, Z0, n)
print("Keystream bits:", keystream)
