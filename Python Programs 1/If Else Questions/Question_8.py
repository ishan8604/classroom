n = int(input("Enter a year\n"))
if n % 4 == 0 and n % 100!=0:
    print("Leap year")
elif n % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap year")
