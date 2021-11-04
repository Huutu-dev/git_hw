def call_sum():
    """ ex1
    Compute the sum of digits in all numbers from 1 to n. When a user enters a number n, find the sum of digits in all numbers from 1 to n.
    Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15
    """

    def sum1(n):
        # Using built-in features
        return sum(range(n + 1))

    def sum2(n):
        # base on Arithmetic progression formula
        return n * (n + 1) / 2

    def sum3(n):
        # pure
        s = 0
        while n > 0:
            s += n
            n -= 1
        return s

    assert sum1(5) == 15
    assert sum2(5) == 15
    assert sum3(5) == 15, sum3(5)

    # Assume the input value is integer
    number = int(input("Enter a number: "))
    print("Result = ", sum3(number))


def call_max():
    """ ex2
    Find max number from 3 values, entered manually from a keyboard.
    Example: 124, 21, 32. Result = 124.
    """

    def max3(snum1: str, snum2: str, snum3: str) -> float:
        # Using built-in features
        return max(float(snum1), float(snum2), float(snum3))

    def max_list(*numerics: float) -> float:
        # pure
        max_num = numerics[0]
        for num in numerics[1:]:
            if max_num < num:
                max_num = num
        return max_num

    # n_max = max3(input("Give first number: "), input("Give second number: "), input("Give third number: "))

    # Assume the input value is number
    n1 = float(input("Give first number: "))
    n2 = float(input("Give second number: "))
    n3 = float(input("Give third number: "))
    print("Result = ", max_list(n1, n2, n3))


def call_classified():
    """ EX3: Count odd and even numbers.====================================================================================
    Count odd and even digits of the whole number.
    Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).
    """
    def part_it1(s_num: str) -> (tuple[int], tuple[int]):
        """Using List comprehension"""
        evens = tuple(int(x) for x in s_num if not int(x) % 2)
        odds = tuple(int(x) for x in s_num if int(x) % 2)
        return evens, odds

    # s_numeric = input("Enter number: ")
    # e, o = part_it1(s_numeric)

    def part_it2(numeric: int) -> (list[int], list[int]):
        evens, odds = [], []
        while numeric:
            x, numeric = divmod(numeric,  10)
            if x % 2:
                odds.append(x)
            else:
                evens.append(x)
        return evens, odds

    digit = int(input("Enter number: "))
    e, o = part_it2(digit)
    print("RESULTS:")
    print("\tEVEN: ", e)
    print("\tODD: ", o)
