n = int(input("Enter a number "))
num1 = int(n / 100)
num2 = int((n % 100) / 10)
num3 = int(n%10)
r = 100*num3 + 10*num2 + num1
print("Reverse is %d" % r)