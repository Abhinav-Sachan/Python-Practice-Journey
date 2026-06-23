x = int(input("Enter the size of the list: "))

n = []
for i in range(x):
    m = int(input("Enter the number: "))
    n.append(m)

target = 100
closest_diff = float('inf')
p = q = None

for i in range(x):
    for j in range(i+1, x):
        current_sum = n[i] + n[j]
        diff = abs(target - current_sum)
        if diff < closest_diff:
            closest_diff = diff
            p, q = n[i], n[j]

if x < 2:
    print("Pair doesn't exist")
else:
    print(p, "&", q, "pair is closest to 100 with sum:", p + q)
