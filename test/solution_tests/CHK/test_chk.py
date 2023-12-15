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
    def test_invalid(self):
        assert checkout_solution.checkout("a") == -1
    def test_new_offer(self):
        assert checkout_solution.checkout("AAAAA") == 200
    def test_two_for_one(self):
        assert checkout_solution.checkout("BEE") == 80
    def test_two_for_one_double(self):
        assert checkout_solution.checkout("BBEEEE") == 160
    def test_f_offer_less_than_3_items(self):
        assert checkout_solution.checkout("FF") == 20
    def test_f_offer_3_items(self):
        assert checkout_solution.checkout("FFF") == 20
    def test_failed_f(self):
        assert checkout_solution.checkout("FFFF") == 30
        assert checkout_solution.checkout("FFFFFF") == 40
