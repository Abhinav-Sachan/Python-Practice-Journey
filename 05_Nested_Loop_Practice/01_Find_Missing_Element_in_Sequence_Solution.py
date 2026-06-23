x = int(input("Enter the size of the list: "))

n = []

for i in range(x):
    m = int(input("Enter the number: "))
    n.append(m)

found = False

for i in range(x - 1):
    if n[i + 1] - n[i] > 1:
        print("Missing number:", n[i] + 1)
        found = True
        break

if not found:
    print("No missing element found")