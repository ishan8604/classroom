u=int(input("Enter the number of units consumed "))
if u<=50:
      bill=u*0.50
elif u>50 and u<=150:
      bill=u*0.75+(50*0.50)
elif u>150 and u<=250:
      bill=u*1.25+(150*0.75)+(50*0.50)
else:
      bill=u*1.50+(150*0.75)+(50*0.50)+(250*1.25)
p=0.20*bill
bill=bill+p
print("Bill: ",bill)
