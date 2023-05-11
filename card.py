from const import RANKS, SUITS


class Card:
    def __init__(self, suit, rank):
        if suit not in SUITS:
            raise ValueError(f"Sorry, suit needs to be one of: {SUITS}")
        if rank not in RANKS:
            raise ValueError(f"Sorry, rank needs to be one of: {RANKS}")
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank}{self.suit}"

    def __str__(self):
        return self.__repr__()  # calling self.repr since they do the same thing

    def __eq__(self, other):
        return self.rank == other.rank  # returns True or False

    def __lt__(self, other):
        return RANKS.index(self.rank) < RANKS.index(other.rank)

if __name__ == "__main__":  # for the code not to run when imported to another file
    # ♣", "♦", "♥", "♠"
    c1 = Card("♦", "7")
    print(c1)
    try:
        c2 = Card("X", "22")
        print(c2)
    except ValueError:
        print("Unable to create card")
    c3 = Card("♥", "7")
    print(f"{c1} = {c3} {c1 == c3}")
    c4 = Card("♥", "8")
    print(f"{c1} > {c4} {c1 > c4}")