#Write a program in python to multiply a number by 32 using bitwise operator only
x=int(input("Enter the number to be multiplied by 32"))
p=(x<<5)
print("%d multiplies by 32 is %d"%(x,p))