x = int(input("Enter the size of list: "))

n = []
for i in range(x):
    m = int(input("Enter the number: "))
    n.append(m)

is_sorted = True
for i in range(0,x-1):
    if n[i] > n[i+1]:
        is_sorted = False
        break

if is_sorted:
    print("List is sorted")
else:
    print(("List is not sorted"))