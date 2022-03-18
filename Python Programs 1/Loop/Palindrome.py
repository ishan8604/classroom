n = int(input("Enter a number\n"))
a = n
r = 0
while n != 0:
    d = int(n % 10)
    r = int(r * 10 + d)
    n = n // 10
if r == a:
    print("Palindrome")
else:
    print("Not")
