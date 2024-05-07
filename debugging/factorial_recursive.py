#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a given number using a recursive approach.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the integer n.
    """
    if n == 0:  # Base case: the factorial of 0 is 1
        return 1
    else:  # Recursive case: n multiplied by the factorial of (n-1)
        return n * factorial(n-1)

# Takes an integer from command line argument, calculates its factorial, and prints it
f = factorial(int(sys.argv[1]))
print(f)