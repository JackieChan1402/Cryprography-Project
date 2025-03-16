import math


def modInverse(a, b):
    if math.gcd(a, b)>1:
        return -1
    for i in range(1, b):
        if (((a%b) * (i % b)) % b == 1):
            return i
    return -1
def main():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    s= a%b
    print(f"Number {a} mod {b} = {s}")

    print(pow(a,-1,b))
if __name__ == '__main__':
    main()
