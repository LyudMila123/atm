import unittest

from features import *

class TestFeatures(unittest.TestCase):

    def setUp(self):
        self.my_features = Atm()
        self.atm_balance = 10000
        self.attempts = 2
        self.correct_pin = 777

    def test_rise_money(self):
        self.assertTrue(self.my_features.rise_money(1000))

    def test_rise_money_fact_equal(self):
        self.my_features.enter_pin(self.correct_pin)
        self.my_features.rise_money(500)
        self.assertEqual(self.my_features.rise_money(500), self.atm_balance+500)

    def test_rise_money_fact_not_equal(self):
        self.my_features.enter_pin(self.correct_pin)
        self.my_features.rise_money(500)
        self.assertNotEqual(self.atm_balance, self.my_features.rise_money(500))

    def test_rise_money_add_null(self):
        self.my_features.enter_pin(self.correct_pin)
        self.my_features.rise_money(0)
        self.assertEqual(self.atm_balance, self.my_features.rise_money(0))


    def test_enter_pin_correct_true(self):
        self.assertTrue(self.my_features.enter_pin(self.correct_pin))

    def test_enter_pin_correct_equal(self):
        my_pin_correct = self.my_features.enter_pin(self.correct_pin)
        self.assertEqual(my_pin_correct, True)

    def test_enter_pin_incorrect(self):
        self.my_features.enter_pin(self.correct_pin)
        self.assertNotEqual(999, self.correct_pin)

    def test_my_enter_pin_correct_not_equal(self):
        self.assertNotEqual(self.my_features.enter_pin(self.correct_pin), IncorrectPin)

    def test_my_enter_pin_correct_not_equal_null(self):
        self.assertNotEqual(self.my_features.enter_pin(self.correct_pin), AttemptsOver)

    def test_get_money(self):
        self.my_features.enter_pin(self.correct_pin)
        self.assertTrue(self.my_features.get_money)

    def test_get_money_equal(self):
        self.my_features.enter_pin(self.correct_pin)
        self.assertEqual(self.my_features.get_money(9500), self.atm_balance - 500)

    def test_check_balance(self):
        self.my_features.enter_pin(self.correct_pin)
        self.assertTrue(self.my_features.check_balance)


















        # my_test_rise_money = self.my_features.rise_money(1000)

