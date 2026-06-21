x = int(input("Enter the size of the list: "))

n = []
for i in range(x):
    m = int(input("Enter the number: "))
    n.append(m)

k = int(input("Enter the index at which number is to be inserted: "))
h = int(input("Enter the number to be inserted: "))

t = []
for i in range(k, len(n)):
    t.append(n[i])

n = n[:k]

n.append(h)

for num in t:
    n.append(num)

print("Updated list:", n)
