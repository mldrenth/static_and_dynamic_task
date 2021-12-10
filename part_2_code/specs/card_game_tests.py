import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_ace = Card("Heart", 1)
        self.card_two = Card("Heart", 2)
        self.card_three = Card("Heart", 3)
        self.cardgame = CardGame()
    
    def test_cardgame_card_for_ace(self):
        result = self.cardgame.check_for_ace(self.card_ace)
        result2 = self.cardgame.check_for_ace(self.card_two)
        self.assertEqual(True, result)
        self.assertEqual(False, result2)
    
    def test_return_highest_card(self):
        result = self.cardgame.highest_card(self.card_two, self.card_three)
        self.assertEqual(self.card_three, result)

    def test_find_total_card_value_amount(self):
        cards = [self.card_ace, self.card_two, self.card_three]
        result = self.cardgame.cards_total(cards)
        self.assertEqual("You have a total of 6", result)