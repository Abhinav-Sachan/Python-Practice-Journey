n = int(input("Enter the no. : "))

if n <= 1:
    print(n, "is not a prime no.")
else:
    is_prime = True   

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:        
            is_prime = False  
            break             

    if is_prime:
        print(n, "is a prime no.")
    else:
        print(n, "is not a prime no.")
