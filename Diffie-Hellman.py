
def main():
    p = int(input("Enter the prime number: "))
    alpha = int(input("Enter the generator number: "))
    a = int(input("Enter the private key: "))
    b = int(input("Enter the private key: "))
    Ka = pow(alpha, a) % p
    Kb = pow(alpha, b) % p
    Kab = pow(Ka, b) % p
    Kba = pow(Kb, a) % p
    print(f"The public key for A is: {Ka}")
    print(f"The public key for B is: {Kb}")
    if Kab == Kba:
        print(f"The Common key is: {Kab}")
    else:
        print("Some thing Wrong!!")

if __name__ == "__main__":
    main()
