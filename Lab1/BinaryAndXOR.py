def DecimalToBinary(num):
    if num >=1:
        DecimalToBinary(num//2)
    print(num%2, end = '' )

def main():
    a = int( input("Enter a number a: "))
    b = int( input("Enter a number b: "))
    DecimalToBinary(a)
    print("\n")
    DecimalToBinary(b)
    print("\n")
    xor = a ^ b
    print(xor)
    print("\n")
    DecimalToBinary(xor)

if __name__ == '__main__':
    main()
