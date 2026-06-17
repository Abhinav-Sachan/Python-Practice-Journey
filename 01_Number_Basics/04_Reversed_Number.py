n = int(input("Enter the number: "))

negative = False

if n < 0:
    negative = True

n = abs(n)
reversed_number = 0

while n > 0:
    digit = n % 10
    reversed_number = reversed_number * 10 + digit
    n //= 10

if negative:
    print(-reversed_number)
else:
    print(reversed_number)