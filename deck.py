from card import Card
from const import *  # * means everything
import random

class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def __repr__(self):
        text = "Deck: "
        for card in self.cards:
            text += f"{card} "
        return text

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop(0)  # position zero of the deck

if __name__ == "__main__":
    deck = Deck()
    print(deck)
    deck.shuffle()
    print("After the shuffle:")
    print(deck)
    print(deck.deal())
    print(deck)  # the popped card is no longer in the deck
