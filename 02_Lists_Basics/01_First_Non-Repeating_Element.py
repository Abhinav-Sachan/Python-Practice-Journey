x = int(input("Enter the size of the list : "))

n = []
for i in range(0,x):
    m = int(input("Enter the no. : "))
    n.append(m)

for i in range(0,x):
        count = 0
        for j in range(0,x):
              if i!=j and n[i]==n[j]:
                    count += 1
        if count == 0:
            print(n[i])
            break
else:
      print("No non repeating element")