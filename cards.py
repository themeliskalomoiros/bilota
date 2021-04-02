from stacks import Stack


ranks = ['A', '10', 'K', 'Q', 'J', '9', '8', '7']
suits = ['Diamonds', 'Clubs', 'Hearts', 'Spades']


class Card:
    """A french-suited playing card."""

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


