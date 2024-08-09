#!/usr/bin/python3
"""this module contain isWinner function to determine who is
the winner of prime game"""


def sieve_of_eratosthenes(n):
    """Generate a list of prime numbers up to n
    using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return [p for p in range(2, n + 1) if is_prime[p]]


def isWinner(x, nums):
    """
    Maria and Ben are playing a game.
    Given a set of consecutive integers starting from 1 up to and including n,
    they take turns choosing a prime number from the set and removing that
    number and its multiples from the set.
    The player that cannot make a move loses the game.

    Args:
      x : the number of rounds
      nums : list contains x of n
    Return:
      winner name (Ben, Maria) or None if draw
    """
    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_set = set(primes)
        available_numbers = set(range(1, n + 1))
        turn = 0  # Maria's turn is even, Ben's turn is odd

        while True:
            current_primes = [p for p in primes_set if p in available_numbers]
            if not current_primes:
                if turn % 2 == 0:
                    ben_wins += 1
                else:
                    maria_wins += 1
                break

            chosen_prime = current_primes[0]
            multiples = set(range(chosen_prime, n + 1, chosen_prime))
            available_numbers -= multiples
            turn += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
