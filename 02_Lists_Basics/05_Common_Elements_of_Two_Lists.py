x = int(input("Enter the size of the list : "))

n = []
t = []
g = []
print("Enter elemnet of list 1 : ")
for i in range(0,x):
    m = int(input("Enter the no. : "))
    n.append(m)
print("Enter elemnet of list 2 : ")
for i in range(0,x):
    k = int(input("Enter the no. : "))
    t.append(k)

for num in n:
    if num in t and num not in g:
        g.append(num)
print(g)