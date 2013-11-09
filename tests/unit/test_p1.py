from unittest import TestCase

from p1 import sum_of_divisors

class TestP1(TestCase):
    def test_sum_multiple_of_3_and_5(self):
        result = sum_of_divisors(1000)
        self.assertEquals(233168, result)
