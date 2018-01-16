import random


# game function
def game():
    # User selects range of numbers
    a = int(input('From: '))
    b = int(input('To: '))
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
start = input('Press Enter / Return to start, or press Q to quit').lower()
if start != 'q':
    game()
