from cards import get_baza_points


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


class Team:
    """A Team in Bilota has two Players."""

    def __init__(self, name, player1, player2):
        self.name = name
        self.player1 = player1
        self.player2 = player2
        self.bazes = []
        self.total_score = 0

    def add_baza(self, baza):
        """Takes a tuple of 4 Cards (baza) and adds it to the list."""
        if self.bazes < 8:
            self.bazes.append(baza)

        raise RuntimeError(f'Team {self.name} has already all bazes.')

    def get_bazes_points(self, suit_of_kozia):
        """Returns the points of the Team's bazes in a current Bilota game."""
        points = 0

        for b in self.bazes:
            points += get_baza_points(b, suit_of_kozia)

        return points

    def save_game_score(self, suit_of_kozia):
        """Saves the points of the game"""
        self.total_score += self.get_bazes_points(suit_of_kozia)
