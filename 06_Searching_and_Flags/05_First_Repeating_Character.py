n = input("Enter the words : ")

k = []
for ch in n:
    k.append(ch)

found = False
for i in range(0, len(k)):
    for j in range(i+1, len(k)):
        if k[i] == k[j]:
            print(k[i], "is the first repeating element")
            found = True
            break
    if found == True:
        break

if found == False:
    print("There is no repeating element")
