from deck import Deck

class PokerHand:
    def __init__(self, deck: Deck):
        self.cards = []
        for _ in range(5):
            self.cards.append(deck.deal())

    def __repr__(self):
        text = ""
        for c in self.cards:
            text += f"{c} "
        return text

    def is_flush(self):
        for c in self.cards[1:]:
            if self.cards[0].suit != c.suit:
                return False
        return True



counter = 0
for _ in range(1000):
    while True:
        counter += 1
        deck = Deck()
        deck.shuffle()
        hand1 = PokerHand(deck)
        if hand1.is_flush():
            # print(hand1)
            # print(f"It took {counter} tries")
            break
print(f"Computed flush probability is: {1000*100/counter}%")