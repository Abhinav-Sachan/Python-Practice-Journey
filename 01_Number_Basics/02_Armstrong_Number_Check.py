n = int(input("Enter the number: "))

if n < 0:
    print(n, "is not an Armstrong number")
else:
    original_number = n

    if n == 0:
        digit_count = 1
    else:
        digit_count = 0
        temp = n

        while temp > 0:
            digit_count += 1
            temp //= 10

    armstrong_sum = 0
    temp = n

    while temp > 0:
        digit = temp % 10
        armstrong_sum += digit ** digit_count
        temp //= 10

    if original_number == 0:
        armstrong_sum = 0

    if armstrong_sum == original_number:
        print(original_number, "is an Armstrong number")
    else:
        print(original_number, "is not an Armstrong number")