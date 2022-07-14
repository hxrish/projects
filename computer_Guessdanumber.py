import random

def computer(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
     guess = random.randint(low, high)
     print(guess)
     usr_input = input("'L' for low, 'C' for correct, 'H' for high: ").lower()
     if usr_input == 'l':
        guess = low + 1
     elif usr_input == 'h':
        guess = high - 1
     elif usr_input == 'c':
        break
    
    print('Congrats!')

computer(20)