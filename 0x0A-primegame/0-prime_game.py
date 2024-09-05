#!/usr/bin/python3

def sieve_of_eratosthenes(n):
    """Generates a list of prime numbers"""
    prime = [True] * (n + 1)
    prime[0], prime[1] = False, False
    i = 2
    while i * i <= n:
        if prime[i]:
            for i in range(i * i, n + 1, i):
                prime[i] = False
        i += 1
    return [i for i in range(n + 1) if prime[i]]

def isWinner(x, nums):
    """Determine the winner of each game based on the rounds played"""
    if x <= 0 or not nums:
        return None

    # Precompute prime up to the largest number in nums
    max_num = max(nums)
    prime = sieve_of_eratosthenes(max_num)
    
    # Track wins for Maria and Ben
    maria_wins, ben_wins = 0, 0

    # For each round, determine who wins
    for n in nums:
        # Count how many prime are <= n
        prime_count = sum(1 for prime in prime if prime <= n)

        # Maria wins if prime_count is odd, Ben wins if it's even
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
