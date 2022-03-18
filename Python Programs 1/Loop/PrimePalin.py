n = int(input("Enter a number\n"))
a = n
c = 0
r = 0
for i in range(1, n+1):
    if n % i == 0:
        c += 1
while n != 0:
    d = int(n % 10)
    r = int(r * 10 + d)
    n = n // 10
if c == 2 and r == a:
    print("Prime Palindrome number")
else:
    print("Not a Prime Palindrome number")
