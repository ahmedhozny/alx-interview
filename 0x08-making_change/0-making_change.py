#!/usr/bin/python3
"""
Making Change Module

This module provides a function to determine the
fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Parameters:
    coins (list of int): A list of the values of the coins in your possession.
    total (int): The total amount to be met using the fewest number of coins.
    """
    if total < 1:
        return 0
    if len(coins) < 1:
        return -1
    coins = sorted(coins, reverse=True)
    if total < coins[-1]:
        return -1

    for attempt in range(len(coins)):
        res = 0
        for coin in coins[attempt:]:
            while total >= coin:
                total -= coin
                res += 1
        if total == 0:
            return res

    return -1
