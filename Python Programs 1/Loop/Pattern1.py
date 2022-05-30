n = int(input("Enter the number of rows\n"))
sp = n
for i in range(1, n + 1):
    print(" "*sp + "* "*i, end = ' ')
    print()
    sp -= 1
sp1 = 2
for i in range(n - 1, 0, -1):
    print(" "*sp1 + "* "*i, end = ' ')
    print()
    sp1 += 1
