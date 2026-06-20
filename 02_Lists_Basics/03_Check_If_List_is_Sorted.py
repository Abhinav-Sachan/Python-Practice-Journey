x = int(input("Enter the size of the list : "))

n = []

for i in range(0,x):
    m = int(input("Enter the no. : "))
    n.append(m)

is_sorted = True
for i in range(0,x):
    for j in range(i+1,x):
        if (n[i]>n[j]):
            is_sorted = False
            break

if (sorted == False):
    print("List is not sorted")
else:
    print("List is sorted")    