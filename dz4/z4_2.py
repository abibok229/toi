def prime_generator():
    n = 2
    while True:
        is_prime = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1

gen = prime_generator()
for _ in range(10):
    print(next(gen))
