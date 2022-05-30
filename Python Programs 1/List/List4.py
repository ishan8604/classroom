#Enter the elements from the user and find out the sum of all the negative elements in list
n = int(input("Enter the number of elements in the list\n"))
lst = []
s = 0
for i in range(n):
    lst.append(int(input("Enter a number\n")))
print(lst)
for i in range(n):
    if lst[i] < 0:
        s = s + lst[i]
print("Sum of all the negative elements: ", s)
