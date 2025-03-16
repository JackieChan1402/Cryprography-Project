def decimalToBinary(num):
    if num >= 1:
        return decimalToBinary(num // 2) + str(num % 2)
    else:
        return '0' if num == 0 else ''
if __name__ == '__main__':
    x = 856
    H =25
    H = decimalToBinary(H)
    n = 7

    if(int(H[0])==0):
        H = H[1:]
    t = len(H)-1

    r = x
    for i in range(t-1, -1, -1):
        r = (r**2) % n
        if H[i]=='1':
            r = (r*x) % n
            print(r)

