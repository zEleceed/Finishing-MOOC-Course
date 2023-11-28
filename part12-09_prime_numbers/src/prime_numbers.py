def prime_numbers():
    num = 2  # The first prime number
    while True:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:  # If num is divisible by any number between 2 and sqrt(num), it is not prime
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1
