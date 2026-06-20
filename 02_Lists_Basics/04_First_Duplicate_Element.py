x = int(input("Enter the size of the list : "))

n = []

for i in range(0,x):
    m = int(input("Enter the no. : "))
    n.append(m)
found = False
for i in range(0,x):
    for j in range(i+1,x):
        if(n[i]==n[j]):
            print(n[i],"is the first duplicate")
            found = True
    if found == True:
        break
if found==False:
    print("There is no duplicate")