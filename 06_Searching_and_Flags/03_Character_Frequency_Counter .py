n = input("Enter the word : ")

visited = []
for i in range(len(n)):
    if n[i] not in visited:
        count = 0
        for j in range(len(n)):
            if n[i] == n[j]:
                count += 1
        visited.append(n[i])
        print(n[i], "->", count)
