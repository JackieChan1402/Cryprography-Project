
def main():
    msg = input("Enter a message: ")
    binary_values = [format(ord(char), '08b') for char in msg]

    # Join the binary values together to get the full binary string
    binary_string = ''.join(binary_values)

    # Print the result
    print(binary_string)
    decimal_value = int(binary_string, 2)
    print(decimal_value)
if __name__ == "__main__":
    main()
