#Write a program in python to multiply a number by 33 using bitwise operator only
x=int(input("Enter the number to be multiplied by 33"))
p=(x<<5)+x
print("%d when multiplied by 33 gives %d"%(x,p))