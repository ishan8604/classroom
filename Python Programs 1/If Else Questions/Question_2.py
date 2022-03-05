a = int(input("Enter a number\n"))
b = int(input("Enter another number\n"))
if a > b:
    print("{} subtracted from {} is {}".format(b, a, (a-b)))
else:
    print("{} subtracted from {} is {}".format(a, b, (b - a)))