import math

# Function to calculate the modular inverse of a number
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Function to generate RSA key pair
def generate_keypair(p, q, e=None, d=None):
    n = p * q
    phi = (p - 1) * (q - 1)

    if e is None and d is None:
        e = 14
    if e is None and d is not None:
        e = math.gcd(d,phi)  # Default public exponent
    if d is None:
        d = mod_inverse(e, phi)  # Calculate private exponent

    return ((e, n), (d, n))

# Function to encrypt a message
def encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)

# Function to decrypt a ciphertext
def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)

# Test Case 1
p1, q1, e1, M1 = 41, 17, 49, 600
public_key1, private_key1 = generate_keypair(p1, q1, e1)
print("Public Key (e, n):", public_key1)
print("Private Key (d, n):", private_key1)
C1 = encrypt(M1, public_key1)
print("Ciphertext C for M =", M1, "is:", C1)
decrypted_M1 = decrypt(C1, private_key1)

# Test Case 2
p2, q2, d2, C2 = 41, 17, 209, 100
public_key2, private_key2 = generate_keypair(p2, q2, d=d2)
print("\nPublic Key (e, n):", public_key2)
print("Private Key (d, n):", private_key2)
decrypted_C2 = decrypt(C2, private_key2)
print("Decrypted plaintext M for C =", C2, "is:", decrypted_C2)
