x = int(input("Enter the size of the list : "))
t = []
n = []
for i in range(0,x):
    m = int(input("Enter the no. : "))
    n.append(m)

for num in n:
    if num not in t:
        t.append(num)

print(t)
