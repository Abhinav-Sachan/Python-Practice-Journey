x = int(input("Enter the size of the list: "))

n = []
t = []
for i in range(x):
    m = int(input("Enter the number: "))
    n.append(m)

k = int(input("Enter the number to be replaced: "))
h = int(input("Enter the replacing number: "))

c = -1
for i in range(x):
    if n[i] == k:
        c = i
        break

if c == -1:
    print("Number not found!")
else:
    for i in range(c):
        t.append(n[i])

    t.append(h)

    for i in range(c+1, x):
        t.append(n[i])

    print("Updated list:", t)
