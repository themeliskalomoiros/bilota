class Player:
    """One of the four players that will participate in a game of Bilota."""

    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card_to_hand(self, card):
        if len(self.hand) < 8:
            self.hand.append(card)

        raise RuntimeError(f'Player\'s {self.name} hand is full.')

    def get_card_from_hand(self, index):
        if self.hand:
            return self.hand.pop(index)

        raise RuntimeError(f'Player\'s {self.name} hand is empty.')
