def isWinner(x, nums):
    if not nums or x < 1:
        return None
    
    # Find the maximum value of n in nums to calculate primes up to that value
    max_num = max(nums)
    
    # Use the Sieve of Eratosthenes to determine all primes up to max_num
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes
    
    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False
    
    # Precompute the number of primes up to each index n
    primes_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        primes_count[i] = primes_count[i - 1] + (1 if sieve[i] else 0)
    
    # Maria wins if the number of primes up to n is odd, Ben wins if it's even
    maria_wins = 0
    ben_wins = 0
    
    for n in nums:
        if primes_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
