def below_mean(numerics: list) -> list:
    """Below The Arithmetical Mean
    When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
    The arithmetical mean is the sum of all elements divided by the number of elements.
    :param numerics: eg [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25)
    :return: eg [1, 3, 4, 2, 3]
    """
    mean_value = sum(numerics) / len(numerics)
    return [x for x in numerics if x < mean_value]


assert below_mean([1, 3, 5, 6, 4, 10, 2, 3]) == [1, 3, 4, 2, 3]


def two_lowest(numerics: list) -> tuple:
    """Two Lowest Elements
    When given a list of elements, find the two lowest elements.
    They can be equal to each other or different.
    :param numerics: eg [198, 3, 4, 9, 10, 9, 2]
    :return: eg (2, 3)
    """
    assert len(numerics) >= 2
    a = b = float('inf')
    for x in numerics:
        if x >= b:
            continue
        if x < a:
            a, b = x, a
        else:
            b = x
    return a, b


assert two_lowest([198, 3, 4, 9, 10, 9, 2]) == (2, 3)
