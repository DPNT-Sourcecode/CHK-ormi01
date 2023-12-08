from solutions.SUM import sum_solution
import unittest

class TestSum(unittest.TestCase):
    def test_sum_with_valid_numbers(self):
        assert sum_solution.compute(1, 2) == 3
    def test_sum_with_invalid_numbers(self):
        self.assertRaises(ValueError, sum_solution.compute(-1,2))

