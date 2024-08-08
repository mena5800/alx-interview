#!/usr/bin/python3
"""this module contain isWinner function to determine who is
the winner of prime game"""


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
    Ben = 0
    Maria = 0

    max_num = max(nums)

    primes = [i for i in range(1, max_num + 1)]
    i = 1
    mul = 2
    while primes:
        while primes[i] * mul <= max_num:
            if primes[i] * mul in primes:
                primes.remove(primes[i] * mul)
            mul += 1

        i += 1
        mul = 2
        if i == len(primes):
            break

    nums.sort()
    i = 1
    # ben 0 - maria 1
    win = [0]
    turn = 1

    for i in range(1, len(primes) - 1):
        win.extend([turn] * (primes[i + 1] - primes[i]))
        turn = 0 if turn == 1 else 1

    if len(win) != max_num:
        win.extend([win[-1]] * (max_num - len(win)))

    for num in nums:
        if win[num - 1] == 0:
            Ben += 1
        else:
            Maria += 1

    if Maria > Ben:
        return "Maria"
    elif Maria < Ben:
        return "Ben"

    return None
