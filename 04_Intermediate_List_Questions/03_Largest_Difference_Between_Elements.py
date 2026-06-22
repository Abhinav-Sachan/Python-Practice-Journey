x = int(input("Enter the size of the list: "))

n = []
for i in range(x):
    m = int(input("Enter the number: "))
    n.append(m)

smallest = float('inf')
largest = float('-inf')

for num in n:
    if num>largest:
        largest = num
    if num<smallest:
        smallest = num

if x == 0:
    print("List is empty")

elif x == 1:
    print("Largest difference: 0")

else:
    print("Largest difference:", largest - smallest)