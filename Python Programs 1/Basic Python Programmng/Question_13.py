p=float(input("Enter the principle amount\n"))
r=float(input("Enter the rate of interest\n"))
t=int(input("Enter the time\n"))
si=(p*r*t)/100.0
a=si+p
print("Simple Interest: ",si)
print("Amount :",a)