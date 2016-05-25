# coding: utf-8

def average(*numbers):
    '''
    计算输入的若干个数字的平均值.

    >>> average(1, 2, 3)
    2.0

    >>> average(0)
    0.0

    >>> average(2, 5)
    3.5
    '''
    return sum(numbers) / len(numbers)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
