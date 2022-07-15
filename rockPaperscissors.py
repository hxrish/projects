import random

def rps():
    user = input('Choice between, (r) Rock, (p) paper, (s) scissors: ').lower()
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
     print(f'It\'s a tie. both you and computer chose {user}')

    elif is_win(user, computer):
        print(f'You won! Computer choose {computer}')

    else:
        print(f'You lost! Computer choose {computer}')

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True
    else:
        return False

rps()