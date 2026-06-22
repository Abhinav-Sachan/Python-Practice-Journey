x = int(input("Enter the size of the list: "))

n = []
for i in range(x):
    m = int(input("Enter the number: "))
    n.append(m)

smallest = float('inf')
p = q = None

for i in range(x):
    for j in range(i+1, x):
        diff = abs(n[i] - n[j])
        if diff < smallest:
            smallest = diff
            p = n[i]
            q = n[j]

if x < 2:
    print("Pair doesn't exist")
else:
    print(p, "&", q, "are the smallest difference pair")
