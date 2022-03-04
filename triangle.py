x=int(input("Enter 1st side"))
y=int(input("Enter 2nd side"))
z=int(input("Enter 3rd side"))
if x+y>z or y+z>x or z+x>y:
      print("Triangle is possible")
else:
      print("Not Possible")
