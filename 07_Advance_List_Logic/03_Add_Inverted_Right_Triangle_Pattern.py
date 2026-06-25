n = int(input("Enter the row : "))

for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()