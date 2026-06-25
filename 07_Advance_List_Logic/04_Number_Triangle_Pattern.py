n = int(input("Enter the row : "))

for i in range(n):
    c = 0
    for j in range(i+1):
        c+=1
        print(c,end=" ")
    print()