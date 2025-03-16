def check_float_deciemal(num):
    if isinstance(num, float):
        decimal_path = num %1
        if decimal_path == 0:
            return True
        else:
            return False
a = int(input("number Phi: "))

b = int(input("number e: "))
for i in range(a):
    d = (1+a*i)/b
    if check_float_deciemal(d):
        if d > a:
            break
        print(d)
        print("\n")



