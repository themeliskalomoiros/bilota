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
        self.cards = Stack()
        for s in suits:
            for r in ranks:
                self.cards.push(Card(r, s))

    def shuffle(self):
        """Shuffles the Deck only if it has max size."""
        if self.cards.size() == 32:
            shuffle(self.cards.items)

        raise RuntimeError('Only a full Deck can be shuffled.')

    def get_card(self):
        """Gets a card from the Deck."""
        return self.cards.pop()
