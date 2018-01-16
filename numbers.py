# limit guesses

# add help message
def help_message():
    print("""
Your goal is to guess a secret number from a range of numbers. You define the range at the start of the game \n""")
    start_game()


def play_again():
    restart = input('Press Enter/Return to play again. Press Q to quit').lower()
    if restart != 'q':
        game()


score = []
counter = []


# game function
def game():
    import random
    guesses = []
    print('')
    print('Your current score: {}/{} '.format(len(score), len(counter)))

    # User selects range of numbers
    try:
        a = int(input('Set lower limit: '))
    except ValueError:
        print('That is not a number')
    try:
        b = int(input('Set upper limit: '))
    except ValueError:
        print('That is not a number')

    # secret number is a random number
    secret_num = random.randint(a, b)
    while len(guesses) < 5:
        # Get users input
        print('Number of guesses: {}/5'.format(len(list(guesses))))
        try:
            guess = int(input('Try to guess my secret number: '))
        except ValueError:
            print("That is not a number\n")
            continue
        # Print guess result
        if guess == secret_num:
            print('You are right! My number was {}'.format(secret_num))
            print('')
            counter.append(guess)
            score.append(guess)
            play_again()
        elif guess < secret_num:
            print('')
            print('Wrong! My number is bigger than {}'.format(guess))
            print('')
        elif guess > secret_num:
            print('')
            print('Wrong! My number is smaller than {}'.format(guess))
            print('')
        guesses.append(guess)

    else:
        print('Sorry, You are out of guesses')
        counter.append(guess)
        play_again()


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
