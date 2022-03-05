a = int(input("Enter the 1st number\n"))
b = int(input("Enter the 2nd number\n"))
c = int(input("Enter the 3rd number\n"))
if a > b and a > c:
    print("Greatest number is: ", a)
elif b > a and b > c:
    print("Greatest number is: ", b)
else:
    print("Greatest number is: ", c)