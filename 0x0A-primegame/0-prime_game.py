#!/usr/bin/python3
"""
Prime Numbers Game Module
"""


def is_prime(n):
    """
    Determines if a number is prime.

    Parameters:
    n (int): The number to be checked for primality.
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_nums_generator(offset):
    """
    Generates prime numbers starting from a given offset.

    Parameters:
    offset (int): The starting point for generating prime numbers.
    """
    n = offset
    while True:
        if is_prime(n):
            yield n
        n += 1


def game(x, nums):
    """
    Simulates the game between Maria and Ben based on the given numbers.

    Parameters:
    x (int): The number of rounds to be played.
    nums (list of int): The numbers for each round.

    Returns:
    tuple: A tuple containing the scores of Maria and Ben.
    """
    maria, ben = 0, 0
    offset = 2
    flag = 0

    nums = sorted(nums)
    for i in range(x):
        num = nums[i]
        if num < 2:
            ben += 1
            continue
        for j in prime_nums_generator(offset):
            if j > num:
                offset = j
                break
            flag = (flag + 1) & 1
        if flag == 1:
            maria += 1
        else:
            ben += 1
    return maria, ben


def isWinner(x, nums):
    """
    Determines the winner of the game based on the scores of Maria and Ben.

    Parameters:
    x (int): The number of rounds to be played.
    nums (list of int): The numbers for each round.

    Returns:
    str: The name of the winner, "Maria" or "Ben".
    Returns None if there is no winner.
    """
    maria, ben = game(x, nums)
    if maria > ben:
        return "Maria"
    elif maria < ben:
        return "Ben"
    else:
        return None
