from solutions.CHK import checkout_solution

class TestChk():
    def test_offer_a(self):
        assert checkout_solution.checkout("AAA") == 130
    def test_offer_a_with_remainder(self):
        assert checkout_solution.checkout("AAAA") == 180
    def test_offer_b(self):
        assert checkout_solution.checkout("BB") == 45
    def test_offer_b_with_remainder(self):
        assert checkout_solution.checkout("BBB") == 75
    def test_with_combination(self):
        assert checkout_solution.checkout("AAABB") == 175
    def test_with_c(self):
        assert checkout_solution.checkout("C") == 20