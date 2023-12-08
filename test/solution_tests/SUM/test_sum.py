from solutions.SUM import sum_solution
import pytest

class TestSum():
    def test_sum_with_valid_numbers(self):
        assert sum_solution.compute(1, 2) == 3
    def test_sum_with_invalid_first(self):
        with pytest.raises(ValueError) as value_error:
            sum_solution.compute(-1, 2)
    def test_sum_with_invalid_second(self):
        with pytest.raises(ValueError) as value_error:
            sum_solution.compute(2, -1)
    def test_sum_with_invalid_both(self):
        with pytest.raises(ValueError) as value_error:
            sum_solution.compute(-1, -1)