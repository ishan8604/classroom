#Enter the elements from the user and find out the sum of all the elements in list
n = int(input("Enter the number of elements in the list\n"))
lst = []
sum = 0
print("Enter the elements")
for i in range(n):
    lst.append(int(input()))
print(lst)
print("Sum of the elements")
for i in range(n):
    sum = sum + lst[i]
print(sum)
