x = int(input("Enter the sixe of the list : "))

n = []

for i in range(0,x):
    m = int(input("Enter the no. : "))
    n.append(m)

def smallest_number(n):
    if len(n)==0:
        return None
    else:
        smallest = float('inf')
        for num in n:
            if num<smallest:
                smallest = num
        return smallest

result = smallest_number(n)

if result is None:
    print("List is empty")
else:
    print("Smallest number :",result)