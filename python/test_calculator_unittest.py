import unittest
import calculator

test_mode = "release"


class TestCalculator(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.cal = calculator.Calculator(1)

    def tearDown(self):
        print("teardown")
        del self.cal

    def test_add(self):
        actual = self.cal.add(2)
        expected = 3
        self.assertEqual(actual, expected)

    def test_add_raise(self):
        with self.assertRaises(ValueError):
            calculator.Calculator("2")

    # @unittest.skip("skip test")
    @unittest.skipIf(test_mode == "release", "release mode")
    def test_skip(self):
        actual = self.cal.add(2)
        expected = 3
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
