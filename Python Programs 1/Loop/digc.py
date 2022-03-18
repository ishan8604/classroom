n = int(input("Enter a number\n"))
c = 0
while n != 0:
    d = int(n % 10)
    c += 1
    n = n // 10
print("Number of digits = ", c)
