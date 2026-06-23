x = int(input("Enter the size of the list: "))

n = []

for i in range(x):
    m = int(input("Enter the number: "))
    n.append(m)

repeated = []

for i in range(x):
    for j in range(i + 1, x):

        if n[i] == n[j]:

            if n[i] not in repeated:
                repeated.append(n[i])

            break

if len(repeated) == 0:
    print("No repeated elements")
else:
    print("Repeated elements:", repeated)