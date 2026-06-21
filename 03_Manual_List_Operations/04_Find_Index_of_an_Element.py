x = int(input("Enter the size of the list: "))

n = []
t = []
for i in range(x):
    m = int(input("Enter the number: "))
    n.append(m)
found = False
k = int(input("Enter the number to find its index : "))
for i in range(0,x):
    if (k == n[i]):
        found = True
        print(k,"is found at index :",i)
        break
        
if found == 0:
    print(k,"doesn't exist in the list")
