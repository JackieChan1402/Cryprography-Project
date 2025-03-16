B = [99, 100, 126, 120, 101, 56, 105, 120, 115, 122, 126, 101, 113, 59, 121,
126, 57, 122, 85, 58, 100, 85, 96, 58, 127, 120, 100, 57, 115, 119]

k = 10

def main():
    A = []
    for i in B:
        A.append(i ^ k)
    result = ""
    for i in A:
        result += chr(i)
    print(A)
    print(result)


if __name__ == '__main__':
    main()
