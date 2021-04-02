from people import Player, Team


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


if __name__ == '__main__':
    # TODO: Bug if allow a team with players of the same name.
    # TODO: Don't allow player with None names.

    print('\n\n-- Create Teams --\n')
    print('1. Team Setup')
    team1 = init_team()

    print('\n2. Team Setup')
    team2 = init_team()

    print('\nTeams created.')
    print(f'\t{team1}\n\t{team2}')

    
