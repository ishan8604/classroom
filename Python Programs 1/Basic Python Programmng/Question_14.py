p=float(input("Enter the principle amount\n"))
r=float(input("Enter the rate of interest\n"))
t=int(input("Enter the time\n"))
a=p*((1+(r/100)))**t
ci=a-p
print("Compound Interest: ",ci)
print("Amount: ",a)