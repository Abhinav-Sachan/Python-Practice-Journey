x = int(input("Enter the size of the list: "))

n = []

for i in range(x):
    m = int(input("Enter the number: "))
    n.append(m)

if x < 2:
    print("No product can be found")

else:
    largest = float('-inf')
    p = k = None

    for i in range(x):
        for j in range(i + 1, x):

            product = n[i] * n[j]

            if product > largest:
                largest = product
                p = n[i]
                k = n[j]

    print("Pair:", p, ",", k)
    print("Product:", largest)