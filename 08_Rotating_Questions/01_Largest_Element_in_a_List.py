x = int(input("Enter the size of the list : "))

n = []
for i in range(0,x):
    m = int(input("Enter the no. : "))
    n.append(m)

largest = float('-inf')
for num in n:
    if (num>largest):
        largest = num

print("Largest element :",largest)