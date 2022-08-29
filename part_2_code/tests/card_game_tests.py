import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def test_check_for_ace_true(self):
        test_card = Card("Hearts", 1)
        self.assertEqual(True, CardGame.check_for_ace(self, test_card))

    def test_check_for_ace_false(self):
        test_card_2 = Card("Clubs", 5)
        self.assertEqual(False, CardGame.check_for_ace(self, test_card_2))

    def test_highest_card_card1(self):
        card1 = Card("Spades", 10)
        card2 = Card("Diamonds", 5)
        self.assertEqual(card1, CardGame.highest_card(self, card1, card2))

    def test_highest_card_card2(self):
        card1 = Card("Spades", 3)
        card2 = Card("Diamonds", 5)
        self.assertEqual(card2, CardGame.highest_card(self, card1, card2))

    def test_cards_total(self):
        card1 = Card("Spades", 3)
        card2 = Card("Diamonds", 5)
        card3 = Card("Clubs", 5)
        cards = [card1, card2, card3]
        self.assertEqual("You have a total of 13", CardGame.cards_total(self, cards))