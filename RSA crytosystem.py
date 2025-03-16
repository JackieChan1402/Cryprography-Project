def check_float_deciemal(num):
    if isinstance(num, float):
        decimal_path = num %1
        if decimal_path == 0:
            return True
        else:
            return False

def calculate_e(a,b):
    for i in range(a):
        d = (1 + a * i) / b
        if check_float_deciemal(d):
            if d > a:
                break
            return d

def find_ecryption_exponent(p,q):
    e1 = int(input("Enter the first exponent: "))
    e2 = int(input("Enter the second exponent: "))
    phi = (p - 1) * (q - 1)
    d1 = calculate_e(phi,e1)
    d2 = calculate_e(phi,e2)
    print("The exponent of the first exponent is: ",d1)
    print("The exponent of the second exponent is: ",d2)

def correspoding_key_pair(p,q):
    e = int(input("Enter the encryption exponent: "))
    d = int(input("Enter the decryption exponent: "))
    x = int(input("Enter the plaint text: "))
    N = p * q
    C = pow(x,e) % N
    print("The encryption is: ",C)
    M = pow(C, d) %N
    if M == x:
        print("The decryption is: ",M)
    else:
        print("some thing Wrong!!!")


def main():
    p = int(input("Enter the prime number p: "))
    q = int(input("Enter the prime number q: "))
    find_ecryption_exponent(p,q)
    correspoding_key_pair(p,q)



if __name__ == "__main__":
    main()
