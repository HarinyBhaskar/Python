N = int(input("Enter the value of N: "))

num = 2

print(f"Prime numbers less than or equal to {N} are:")

while num <= N:
    is_prime = True  # Assume current number is prime
    i = 2

    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print(num, end=" ")

    num += 1
