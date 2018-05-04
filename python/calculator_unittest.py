class Calculator(object):
    def __init__(self, x):
        if type(x) is not int:
            raise ValueError
        self.x = x

    def add(self, y):
        """
        Returns the addition result of x and y
        :param y: number
        :return: x + y
        """
        if type(y) is not int:
            raise ValueError
        return self.x + y
