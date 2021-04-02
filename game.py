from random import shuffle
from people import Player, Team
from queues import Queue


def init_team():
    # Get names.
    t = input('\n\tTeam name: ').lower().capitalize()
    p1 = input(
        f'\n\tPlayer name of {t}: ').lower().capitalize()
    p2 = input(
        f'\tPlayer name of {t}: ').lower().capitalize()

    # Format names.
    t = t.lower().capitalize()
    p1 = p1.lower().capitalize()
    p2 = p2.lower().capitalize()

    # Init a Team instance.
    p1 = Player(p1)
    p2 = Player(p2)

    return Team(t, p1, p2)


class Table:
    """The table where the Players of the two Teams are sitting, controlling 
    the Players turns."""

    def __init__(self, team1, team2, player_playing_first):
        self.players = [team1.player1, team2.player1,
                        team1.player2, team2.player2]

        # Init seats
        self.seats = Queue()
        for p in self.players:
            self.seats.enqueue(p)

        # Set player who plays first next
        while not self.seats.peek() == player_playing_first:
            self.get_next_player()

    def get_next_player(self):
        """Returns the player who plays next."""

        player = self.seats.dequeue()
        self.seats.enqueue(player)

        return player

    def __str__(self):
        p1 = f'{self.players[0]}'
        p2 = f'{self.players[1]}'
        p3 = f'{self.players[2]}'
        p4 = f'{self.players[3]}'

        if p1 == self.seats.peek():
            p1 = f'*{p1}*'
        elif p2 == self.seats.peek():
            p2 = f'*{p2}*'
        elif p3 == self.seats.peek():
            p3 = f'*{p3}*'
        else:
            p4 = f'*{p4}*'

        return f'-- Table --\n\n\t\t\t{p1}\n\n\n\t{p2}\t\t\t{p4}\n\n\n\t\t\t{p3}'


if __name__ == '__main__':
    # TODO: Bug if allow a team with players of the same name.
    # TODO: Don't allow player with None names.

    # Init teams.
    print('\n\n-- Create Teams --\n')
    print('1. Team Setup')
    team1 = init_team()

    print('\n2. Team Setup')
    team2 = init_team()

    print('\nTeams created.')
    print(f'\t{team1}\n\t{team2}')

    # Decide which player plays first.
    print('\n\n-- Deciding Player Turns --')
    players = [team1.player1, team2.player1, team1.player2, team2.player2]
    shuffle(players)
    player_playing_first = players[0]
    print(f'\nKing goes to {player_playing_first}!')

    # Init Table
    table = Table(team1, team2, player_playing_first)
    print(table)
