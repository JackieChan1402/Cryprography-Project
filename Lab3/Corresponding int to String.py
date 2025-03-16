 #The given integer
number = int(input("Enter a number: "))
string_lab2 = ""
while number > 0:
    string_lab2 = chr(number %256) + string_lab2
    number //= 256
print(string_lab2)
