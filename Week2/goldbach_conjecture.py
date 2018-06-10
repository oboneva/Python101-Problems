def goldbach(n):
    numbers = [True] * n
    primes = []

    for i in range(2, n):
        if numbers[i]:
            primes.append(i)
            for j in range(i**2, n, i):
                numbers[j] = False

    prime_tupels_list = []

    for i in range(len(primes)):
        if (n - primes[i]) in primes[i:]:
            prime_tupels_list.append((primes[i], n - primes[i]))

    return prime_tupels_list
