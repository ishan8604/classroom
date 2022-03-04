cp=float(input("Enter the Cost Price of the product\n"))
sp=float(input("Enter the Selling Price of the product\n"))
if sp>cp:
      p=sp-cp
      print("Profit: ",p)
      pp=(p/cp)*100
      print("Profit %: ",pp)
else:
      p=cp-sp
      print("Loss: ",p)
      pp=(p/cp)*100
      print("Loss %: ",pp)
