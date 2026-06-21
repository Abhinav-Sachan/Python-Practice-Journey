x = int(input("Enter the size of the list: "))

n = []
t = []
for i in range(x):
    m = int(input("Enter the number: "))
    n.append(m)

k = int(input("Enter the index for deletion : "))

for i in range(0,k):
    t.append(n[i])

for i in range(k+1,x):
    t.append(n[i])

print(t)