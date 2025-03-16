import math
def coprime(a,b):
    return math.gcd(a,b)==1

def numOfArray(arr, n):
    count = 0
    for i in range(0, n -1):
        for j in range(i +1, n):
            if (coprime(arr[i],arr[j])):
                count += 1
                print((arr[i],arr[j]))
    return count

def main():
    A = [290345, 218585, 143231, 164172, 155768, 423151, 239707, 153544, 287390, 480837]
    print(numOfArray(A, len(A)))

if __name__ == "__main__":
    main()
