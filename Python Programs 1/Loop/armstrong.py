n = int(input("Enter a number\n"))
a = n
b = n
c = 0
s = 0
while n != 0:
    d = int(n % 10)
    c += 1
    n = n // 10
while a != 0:
    d = int(a % 10)
    s = s + (d ** c)
    a = a // 10
if s == b:
    print("Armstrong Number\n")
else:
    print("Not an Armstrong number")
