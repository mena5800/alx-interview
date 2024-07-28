#!/usr/bin/python3
"""
this file contain function makeChange
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total.

    Arguments:
      coins : is a list of the values of the coins in your possession
      total : target amount
    Return:
      fewest number of coins needed to meet a given amount total.

    """

    if total <= 0:
        return 0
    dp = [float("inf")] * (total + 1)

    for i in range(1, len(dp)):
        if i in coins:
            dp[i] = 1

        else:
            for coin in coins:
                if dp[i - coin] == float("inf"):
                    continue

                dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[-1] == float("inf") else dp[-1]
