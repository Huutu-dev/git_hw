from functools import cmp_to_key


def even_first(numerics: list):
    """Even First
    Your input is an array of integers, and you have to reorder its entries so that the even entries appear first.
    You are required to solve it without allocating additional storage (operate with the input array).
    :Example: [7, 3, 5, 6, 4, 10, 3, 2]
    :Return: [6, 4, 10, 2, 7, 3, 5, 3]
    """
    numerics.sort(key=cmp_to_key(lambda x, y: (x % 2) - (y % 2)))
    # return just the input array after being operated on itself
    return numerics


assert even_first([7, 3, 5, 6, 4, 10, 3, 2]) == [6, 4, 10, 2, 7, 3, 5, 3]


def increment_number(digits):
    """Increment a Number
    Write a program that takes as input an array of digits encoding a non-negative decimal integer D and updates the array to represent the integer D + 1.
    :Example: if the input is [1, 2, 9]
    :Result: then you should update the array to [1, 3, 0]
    """
    number = int(''.join(map(str, digits)))
    return [int(x) for x in str(number+1)]


assert increment_number([1, 2, 9]) == [1, 3, 0], increment_number([1, 2, 9])
