
def find_signature(P, alpha, d):
    x = int(input("Enter X: "))
    e = int(input("Enter e: "))
    r = pow(alpha, e) % P
    invert_e = pow(e, -1, (P-1))
    s = ((x - d*r)*invert_e) %(P-1)
    print(f"Signature is: ({r}, {s})")

def calculate_valid(P,beta, r,s):
    t = (pow(beta, r) * pow(r,s)) % P
    return t


def check_valid(P, alpha, beta):
    n = int(input("How much input n: "))
    x= []
    r =[]
    s = []
    for i in range(n):
        X = input(f"Enter X{i+1}: ")
        R = input(f"Enter R{i+1}: ")
        S = input(f"Enter S{i+1}: ")
        x.append(X)
        r.append(R)
        s.append(S)
    t = []
    for i in range(n):
        t.append(calculate_valid(P,beta, int(r[i]), int(s[i])))

    for i in range(n):
        if int(t[i]) == (pow(alpha, int(x[i])) %P):
            print(f"{t[i]}")
            print(f"{x[i]} is valid")
        else:
            print(f"{t[i]}")
            print(f"{x[i]} is not valid")

def main():
    d = int(input("Enter d private key : "))
    P = int(input("Enter P public key : "))
    alpha = int(input("Enter alpha public key : "))
    beta = pow(alpha, d) %P
    print(f"beta = {beta}")
    find_signature(P, alpha, d)
    check_valid(P, alpha, beta)

if __name__ == "__main__":
    main()

