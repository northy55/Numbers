import random

# secret number is a random number
secret_num = random.randint(1,10)

# allow multiple guesses
while True:
    # Get users input
    guess = int(input('Try to guess my secret number: '))
    # Print guess result
    if guess == secret_num:
        print('You are right! My number was {}'.format(secret_num))
    else:
        print('Sorry, you\'ve missed it')