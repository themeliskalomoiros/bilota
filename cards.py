class Rank:
    """Includes all the available playing cards for a Bilota game."""

    def __init__(self):
        self.ace = 'A'
        self.ten = '10'
        self.king = 'K'
        self.queen = 'Q'
        self.jack = 'J'
        self.nine = '9'
        self.eight = '8'
        self.seven = '7'


class Suit:
    """Includes all the suits of the playing cards."""

    def __init__(self):
        self.diamonds = 'Diamonds'
        self.clubs = 'Clubs'
        self.hearts = 'Hearts'
        self.spades = 'Spades'


class Card:
    """A french-suited playing card."""

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit


        