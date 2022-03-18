n = int(input("Enter a number\n"))
c = 0
for i in range(1, n + 1):
    c=0
    for j in range(1, i + 1):
        c+=1
        if c == 2:
            print(j)
