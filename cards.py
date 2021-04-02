from random import shuffle
from stacks import Stack


ranks = ['A', '10', 'K', 'Q', 'J', '9', '8', '7']
suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']


class Card:
    """A french-suited playing card."""

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    "A bilota deck of cards."

    def __init__(self):
        self.stack = Stack()
        for s in suits:
            for r in ranks:
                self.stack.push(Card(r, s))

    def shuffle(self):
        if self.stack.size() == 32:
            shuffle(self.stack.items)

        raise RuntimeError('Only a full Deck can be shuffled.')
