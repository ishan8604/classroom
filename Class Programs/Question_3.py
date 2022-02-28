#Write a program check whether last digit of number is 1 or 0
x=int(input("Enter a number to check "))
p=x%2
print(p==1 and "1" or "0")