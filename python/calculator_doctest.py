class Calculator(object):
    @staticmethod
    def add(x, y):
        """
        Returns the addition result of x and y
        :param x: arg1 number
        :param y: arg2 number
        :return: x + y

        >>> Calculator.add(1, 2)
        3

        >>> Calculator.add("1", "2")
        Traceback (most recent call last):
        ...
        ValueError
        """
        if type(x) is not int or type(y) is not int:
            raise ValueError
        return x + y


if __name__ == "__main__":
    import doctest

    doctest.testmod()
