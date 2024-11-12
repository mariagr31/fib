import argparse
from functools import cache


def fibonacci_iterative(n: int):
    """
    Computes the n-th Fibonacci number
    :param n: n-th Fibonacci number
    :return: The n-th Fibonacci number
    """
    if n < 0:
        raise ValueError("n must be greater than or equal to zero")
    if n < 2:
        return n
    n0 = 0
    n1 = 1
    for _ in range(n):
        nth = n0 + n1
        n0 = n1
        n1 = nth
    return n0


""" 
while(cont < n-2):
       result = first_number + second_number
       first_number = second_number
       second_number = result
       cont = cont+1
"""


@cache
def fibonacci_recursive(n: int):
    """
    Computes the n-th Fibonacci number
    :param n: n-th Fibonacci number
    :return: The n-th Fibonacci number
    """
    if n < 0:
        raise ValueError("n must be greater than or equal to zero")
    if n < 2:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

if __name__ == "__main__":  # esto lo ponermos para que solo se imprima cuando estoy llamando al script
    parser = argparse.ArgumentParser()
    parser.add_argument('nth', type=int, help="Nth Fibonacci number.")  # positional argument
    args = parser.parse_args()

    resultado = fibonacci_recursive(args.nth)
    print(resultado)
