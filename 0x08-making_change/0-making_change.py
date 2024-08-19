#!/usr/bin/python3
"""
determine the fewest number of coins
needed to meet a given amount total.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1
        if total == 0:
            return count

    return -1

    """
    penny = 1 cent
    nickel = 5 cent
    dime = 10 cent
    quarter = 25 cent
    """
