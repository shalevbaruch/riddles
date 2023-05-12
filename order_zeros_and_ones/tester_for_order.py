import unittest
from order import order  

class OrderTestCase(unittest.TestCase):
    def test_order(self):
        arr = [0, 1, 0, 1, 1, 0]
        expected_result = [0, 0, 0, 1, 1, 1]
        self.assertEqual(order(arr), expected_result)

    def test_order_with_empty_array(self):
        arr = []
        expected_result = []
        self.assertEqual(order(arr), expected_result)

    def test_order_with_only_zeros(self):
        arr = [0, 0, 0, 0, 0]
        expected_result = [0, 0, 0, 0, 0]
        self.assertEqual(order(arr), expected_result)

    def test_order_with_only_ones(self):
        arr = [1, 1, 1, 1, 1]
        expected_result = [1, 1, 1, 1, 1]
        self.assertEqual(order(arr), expected_result)

    def test_order2(self):
        arr = [1, 1, 1, 1, 0, 1]
        expected_result = [0,1, 1, 1, 1, 1]
        self.assertEqual(order(arr), expected_result)

    def test_order3(self):
        arr = [0, 0, 0, 0, 1, 0]
        expected_result = [0, 0, 0, 0, 0, 1]
        self.assertEqual(order(arr), expected_result)

if __name__ == '__main__':
    unittest.main()
