x = int(input("Enter the size of the list: "))

n = []
for i in range(x):
    m = int(input("Enter the number: "))
    n.append(m)

visited = []
for i in range(x):
    if n[i] not in visited:
        count = 0
        for j in range(x):
            if n[i] == n[j]:
                count += 1
        visited.append(n[i])
        print(n[i], "->", count)
