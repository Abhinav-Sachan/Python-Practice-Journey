x = int(input("Enter the size of the 1st list: "))

n = []
for i in range(x):
    m = int(input("Enter the number: "))
    n.append(m)

y = int(input("Enter the size of the 2nd list: "))

o = []
for i in range(y):
    m = int(input("Enter the number: "))
    o.append(m)

dup1 = []
for i in range(x):
    for j in range(i + 1, x):
        if n[i] == n[j]:
            if n[i] not in dup1:
                dup1.append(n[i])
            break

dup2 = []
for i in range(y):
    for j in range(i + 1, y):
        if o[i] == o[j]:
            if o[i] not in dup2:
                dup2.append(o[i])
            break

common = []
for num in dup1:
    if num in dup2:
        common.append(num)

if len(common) == 0:
    print("No common duplicates found")
else:
    print("Common duplicate elements:", common)