x = int(input("Enter the size of the list: "))

n = []

for i in range(x):
    m = int(input("Enter the number: "))
    n.append(m)

unique = True

for i in range(x):
    for j in range(i + 1, x):

        if n[i] == n[j]:
            unique = False
            break

    if not unique:
        break

if unique:
    print("All elements are unique in the list")
else:
    print("All elements are not unique in the list")