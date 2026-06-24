n = input("Enter the word : ")

visited = []
found = False

for i in range(len(n)):

    if n[i] not in visited:

        count = 0

        for j in range(len(n)):
            if n[i] == n[j]:
                count += 1

        visited.append(n[i])

        if count == 1:
            found = True
            print(n[i], "is the first non repeated character")
            break

if not found:
    print("No non repeated character found")
    