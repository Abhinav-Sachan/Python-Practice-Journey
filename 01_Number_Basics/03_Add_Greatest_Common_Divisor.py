a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

a = abs(a)
b = abs(b)

if a == 0 and b == 0:
    print("GCD is undefined")
else:
    gcd_value = 1

    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd_value = i

    print("GCD of", a, "and", b, "is:", gcd_value)