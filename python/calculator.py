import os


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

    def output(self, dir_path, file_name):
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        file_path = os.path.join(dir_path, file_name)
        with open(file_path, "w") as f:
            f.write("test")
