import random
def guess(x):
    random_number = random.randint(1, x)
    zero = 0
    while zero != random_number:
        usr_input = int(input('Your guess: '))
        if usr_input < random_number:
            print('Sorry, the number is too low!')
        elif usr_input > random_number:
            print('Woops! the number is too high.')
        else:
            break
    print( f'Wohoo! You have successfully guessed the number {random_number}')

guess(10)
