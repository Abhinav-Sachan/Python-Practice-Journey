x = int(input("Enter the size of list: "))

n = []
for i in range(x):
    m = int(input("Enter the number: "))
    n.append(m)

if x == 0:
    print("List is empty")
else:
    smallest = float('inf')

    for num in n:
        if num < smallest:
            smallest = num

    print("Smallest element:", smallest)