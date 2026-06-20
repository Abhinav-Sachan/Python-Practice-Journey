x = int(input("Enter the size of the list : "))

n = []
for i in range(x):
    m = int(input("Enter the no. : "))
    n.append(m)

k = int(input("Enter the element you want to delete : "))

while k in n:
    n.remove(k)

print("Updated list:", n)
