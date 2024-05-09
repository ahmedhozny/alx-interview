#!/usr/bin/python3
"""
Calculates the fewest number of operations needed
"""
dp = {}


def minOperations(n):
    """
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The fewest number of operations needed.
        If n is impossible to achieve, returns 0.
    """
    if n < 2:
        return 0

    return factorize(n, 2)


def factorize(n, factor):
    """
    Recursively factors the given number `n`
    and calculates the minimum number of operations required to reach 1.

    Args:
        n (int): The number to factorize.
        factor (int): The current factor to start factorization.

    Returns:
        int: The minimum number of operations required
        to reach 1 from `n` by factoring and adding factors.
    """
    if n == 1:
        return 0

    if n in dp:
        return dp[n]

    while n % factor != 0:
        factor += 1

    dp[n] = factor + factorize(n // factor, factor)
    return dp[n]
