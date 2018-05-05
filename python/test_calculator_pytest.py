# pytest test_calculator_pytest.py --cov=calculator --cov-report term-missing

import calculator
import os
import pytest
import shutil

test_mode = "release"


def test_add():
    cal = calculator.Calculator(1)
    assert cal.add(2) == 3


def test_custom_fixture(custom_fixture):
    print(custom_fixture)


class TestCalculator(object):
    @classmethod
    def setup_class(cls):
        print("start")
        cls.cal = calculator.Calculator(1)
        cls.test_dir = "./tmp/"
        cls.test_file_name = "test.txt"

    @classmethod
    def teardown_class(cls):
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)
        print("end")

    def setup_method(self, method):
        print("setup {}".format(method.__name__))

    def teardown_method(self, method):
        print("teardown {}".format(method.__name__))

    def test_add(self, request):
        os_name = request.config.getoption("--os-name")
        if os_name == "windows":
            print("windows")
        else:
            print("not windows")

        cal = calculator.Calculator(1)
        assert cal.add(2) == 3

    def test_raise(self):
        with pytest.raises(ValueError):
            calculator.Calculator("1")

    def test_add_raise(self):
        with pytest.raises(ValueError):
            calculator.Calculator(1).add("2")

    def test_output(self, tmpdir):
        self.cal.output(tmpdir, self.test_file_name)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path)

    def test_output_no_dir(self, tmpdir):
        self.cal.output(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(self.test_dir, self.test_file_name)
        assert os.path.exists(test_file_path)

    @pytest.mark.skipif(test_mode == "release", reason="release mode")
    def test_add_skip(self):
        cal = calculator.Calculator(1)
        assert cal.add(2) != 3
