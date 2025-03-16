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
def generate_keypair(p, q, e):
    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

# Function to decrypt a ciphertext
def decrypt(ciphertext, private_key):
    d, n = private_key
    return pow(ciphertext, d, n)

# RSA parameters
p = 81401
q = 27109
e = 65537
ciphertext = 412589464

# Generate key pair
public_key, private_key = generate_keypair(p, q, e)

# Decrypt the ciphertext
decrypted_ascii = decrypt(ciphertext, private_key)

# Convert the decrypted integer to a string
plaintext_string = ""
while decrypted_ascii > 0:
    plaintext_string = chr(decrypted_ascii % 256) + plaintext_string
    decrypted_ascii //= 256

print("Decrypted plaintext string in ASCII code:", plaintext_string)
