import random


# add help message
def help_message():
    print("""
Your goal is to guess a secret number from a range of numbers. You define the range at the start of the game \n""")
    start_game()


# game function
def game():
    # User selects range of numbers
    a = int(input('Set lower limit: '))
    b = int(input('Set upper limit: '))
    # secret number is a random number
    secret_num = random.randint(a, b)
    while True:
        # Get users input
        guess = int(input('Try to guess my secret number: '))
        # Print guess result
        if guess == secret_num:
            print('You are right! My number was {}'.format(secret_num))
            break
        elif guess < secret_num:
            print('Wrong! My number is bigger than {}'.format(guess))
            a = guess + 1
        elif guess > secret_num:
            print('Wrong! My number is smaller than {}'.format(guess))
            a = guess - 1


# Add option to start or Quit the game
def start_game():
    start = input('Press Enter / Return to start, or press Q to quit \n').lower()
    if start != 'q':
        name = input('What is your name? \n')
        # Add help message
        message = input(name + ', welcome to the game of numbers! Do you know how to play? Y/n \n').lower()
        if message != 'n':
            game()
        else:
            help_message()


start_game()
