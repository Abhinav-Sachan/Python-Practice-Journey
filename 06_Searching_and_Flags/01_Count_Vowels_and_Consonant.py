n = input("Enter the word : ")
v = 0
c = 0
for ch in n:
    if ch.isalpha():
        if ch in "aeiouAEIOU":
            v += 1
        else:
            c += 1

print("Vowel :",v)
print("Consonant :",c)