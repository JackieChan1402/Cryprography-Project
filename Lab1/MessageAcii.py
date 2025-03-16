def changeIntToSymbol(num):
    return chr(num)

A= [105, 110, 116, 114, 111, 50, 99, 114, 121, 112, 116, 111, 123, 119, 51,
108, 99, 48, 109, 51, 95, 116, 48, 95, 106, 48, 117, 114, 110, 51, 121, 125]
def main():
    B = ""
    for i in A:
        B = B + changeIntToSymbol(i)
    print(B)
if __name__ == '__main__':
    main()
