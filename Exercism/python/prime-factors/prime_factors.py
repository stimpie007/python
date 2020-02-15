from typing import List

def factors(value):
    """
    Finding the prime factors for given value

    :param:
    value: int

    :return:
    prime_factors: list
    """
    i = 2
    prime_factors = []
    while i * i <= value:
        if value % i:
            i += 1
        else:
            value //= i
            prime_factors.append(i)
    if value > 1:
        prime_factors.append(value)
    return prime_factors
