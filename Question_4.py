n=int(input("Enter a 3 digit number "))
n1=int(n/100)
n2=int((n%100)/10)
n3=int(n%10)
sum=n1+n2+n3
print("Sum of all the digits of the number {}".format(sum))