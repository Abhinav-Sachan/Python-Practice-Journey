x = int(input("Enter the sixe of the list : "))

n = []

for i in range(0,x):
    m = int(input("Enter the no. : "))
    n.append(m)

def largest_number(n):
    if len(n)==0:
        return None
    else:
        largest = float('-inf')
        for num in n:
            if num>largest:
                largest = num
        return largest

if largest_number(n) is None:
    print("List is empty")
else:
    print("Largest number :",largest_number(n))