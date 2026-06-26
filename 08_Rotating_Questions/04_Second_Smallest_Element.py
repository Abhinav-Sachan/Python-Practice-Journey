x = int(input("Enter the size of list: "))

n = []
for i in range(x):
    m = int(input("Enter the number: "))
    n.append(m)

smallest = float("inf")
second_smallest = float("inf")

for num in n:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num<second_smallest and num!=smallest :
        second_smallest = num

if second_smallest == float('inf'):
    print("No second smallest element")
else:
    print("Second smallest element:", second_smallest)