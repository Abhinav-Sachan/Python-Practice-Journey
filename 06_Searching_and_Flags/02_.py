n = input("Enter the words : ")

k = []
h = []
for ch in n:
    k.append(ch)

for i in range(len(k)-1,-1,-1):
    h.append(k[i])

Palindrome = False
if k==h:
    Palindrome = True

if Palindrome == True:
    print(n,"is Palindrome")
else:
    print(n,"is not Palindrome")