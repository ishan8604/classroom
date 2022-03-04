bp=float(input("Enter the basic salary"))
if bp<10000:
      hra=0.80*bp
      ta=0.80*bp
      print("Salary : ",(bp+hra+ta))
elif bp>10000 and bp<=20000:
      hra=0.85*bp
      ta=0.85*bp
      print("Salary : ",(bp+hra+ta))
else:
      hra=0.90*bp
      ta=0.95*ta
      print("Salary : ",(bp+hra+ta))
