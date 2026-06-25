n = int(input("Enter the row : "))
c = 0
for i in range(n):
    c+=1
    for j in range(i+1):
        print(c,end=" ")
    print()