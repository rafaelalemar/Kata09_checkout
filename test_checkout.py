import unittest
from checkout import Checkout
from rules import RULES

__author__ = 'rafael'


class TestCheckout(unittest.TestCase):

    def price(self, goods):
        co = Checkout(RULES)
        for item in list(goods):
            co.scan(item)
        return co.total


    def test_scan(self):
        self.assertEqual(0, self.price(""))
        self.assertEqual(50, self.price("A"))
        self.assertEqual(80, self.price("AB"))
        self.assertEqual(115, self.price("CDBA"))

        self.assertEqual(100, self.price("AA"))
        self.assertEqual(130, self.price("AAA"))
        self.assertEqual(180, self.price("AAAA"))
        self.assertEqual(230, self.price("AAAAA"))
        self.assertEqual(260, self.price("AAAAAA"))

        self.assertEqual(160, self.price("AAAB"))
        self.assertEqual(175, self.price("AAABB"))
        self.assertEqual(190, self.price("AAABBD"))
        self.assertEqual(190, self.price("DABABA"))

        # Teste com itens inexistentes
        self.assertEqual(0, self.price("Z"))
        self.assertEqual(50, self.price("ZA"))