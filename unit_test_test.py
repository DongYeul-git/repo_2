import unittest

import test  # test.py가 같은 디렉토리에 있다고 가정

class TestTestModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(test.add(2, 3), 5)
        self.assertEqual(test.add(-1, 1), 0)
        self.assertEqual(test.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(test.subtract(5, 3), 2)
        self.assertEqual(test.subtract(0, 1), -1)
        self.assertEqual(test.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(test.multiply(2, 3), 6)
        self.assertEqual(test.multiply(-1, 1), -1)
        self.assertEqual(test.multiply(0, 100), 0)

    def test_divide(self):
        self.assertEqual(test.divide(6, 3), 2)
        self.assertEqual(test.divide(-4, 2), -2)
        with self.assertRaises(ZeroDivisionError):
            test.divide(1, 0)

if __name__ == '__main__':
    unittest.main()